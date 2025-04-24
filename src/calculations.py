"""
Модуль calculations.py

Здесь реализуются функции для расчета топографических атрибутов на основе DEM.
"""
import xdem
import os
from pyproj import CRS
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info
from src.utils import combine_xarrays

def get_utm_crs(lat, lon):
    """Получить UTM CRS на основе координат."""
    utm_crs_list = query_utm_crs_info(
        datum_name="WGS 84",
        area_of_interest=AreaOfInterest(
            west_lon_degree=lon,
            south_lat_degree=lat,
            east_lon_degree=lon,
            north_lat_degree=lat,
        ),
    )
    utm_crs = CRS.from_epsg(utm_crs_list[0].code)
    return utm_crs

def calculate_terrain_attributes(dem_path, attributes, path, **kwargs):
    """Рассчитать несколько топографических атрибутов с использованием xdem"""
    # Создаем DEM объект
    dem = xdem.DEM(dem_path, vcrs="WGS84")
    print('Shape of DEM', dem.shape)
    print(dem)
    print('Coordinate system before reprojection', dem.vcrs)
    # Если в dem одна точка, делаем репроекцибю по координатам этой точки
    if dem.shape == (1, 1):
        raise ValueError("ЦМР это точка."
                         "Нельзя посчитать показатели рельефа (для них нужны сосдение пиксели).")
    else:
        # Получаем координаты центра DEM
        center_lat = (dem.bounds.top + dem.bounds.bottom) / 2
        center_lon = (dem.bounds.left + dem.bounds.right) / 2
        # Получаем UTM CRS на основе координат центра DEM
        target_crs = get_utm_crs(center_lat, center_lon)
        print("Coordinate system after reprojection", target_crs)
    # Перепроекция DEM на целевой CRS(coordinate reference system)
    # ЕСЛИ НЕ СДЕЛАТЬ ПЕРЕПРОЕКЦИЮ, то считаться будет плохо
    # В примере перепроекция сделана на EPSG:32637 (это для подмосковья)
    # CRS выбирается в зависимости от региона
    reprojected_dem = dem.reproject(crs=target_crs, res=30)
    # Считаем все атрибуты
    attribute_arrays = reprojected_dem.get_terrain_attribute(attributes, **kwargs)
    # Преобразуем Raster объекты в xarray DataArrays
    attribute_xarrays = list(map(lambda x: x.to_xarray(), attribute_arrays))
    # Добавляем reprojected DEM в список атрибутов (первым)
    attribute_xarrays.insert(0, reprojected_dem.to_xarray())
    attributes.insert(0, "reprojected_dem")
    # Объединим xarray DataArrays в один xarray.Dataset
    combined_xarray = combine_xarrays(attribute_xarrays, attributes)
    combined_xarray.attrs["resolution_m"] = 30
    combined_xarray.attrs["coordinate_system"] = str(target_crs)
    # Сохраняем объединенный xarray на указанный путь
    return combined_xarray
