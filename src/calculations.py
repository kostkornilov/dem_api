import xdem
import rioxarray
import tempfile
import os
import matplotlib.pyplot as plt
from pyproj import CRS
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info

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

def calculate_terrain_attributes(dem_path, attributes, output_dir, **kwargs):
    """Рассчитать несколько топографических атрибутов с использованием xdem и сохранить как TIFF файлы."""
    # Создаем DEM объект
    dem = xdem.DEM(dem_path, vcrs="WGS84")
    print(dem)
    print('Coordinate system before reprojection', dem.vcrs)
    
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
    reprojected_dem.save(os.path.join(output_dir, "reprojected_dem.tif"))
    
    # Считаем все атрибуты
    attribute_arrays = reprojected_dem.get_terrain_attribute(attributes, **kwargs)
    
    # Преобразуем Raster объекты в xarray DataArrays
    attribute_xarrays = list(map(lambda x: x.to_xarray(), attribute_arrays))
    
    # Сохраняем атрибуты как GeoTIFF файлы
    for attribute, attribute_xarray in zip(attributes, attribute_xarrays):
        output_path = os.path.join(output_dir, f"{attribute}.tif")
        attribute_xarray.rio.to_raster(output_path)
    
    # Добавляем reprojected DEM в список атрибутов (первым)
    attribute_xarrays.insert(0, reprojected_dem.to_xarray())
    attributes.insert(0, "reprojected_dem")
    
    return attribute_xarrays

def calculate_slope(dem_path, output_dir):
    """Рассчитать уклон и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    slope = dem.slope()
    return slope

def calculate_hillshade(dem_path, output_dir):
    """Рассчитать hillshade и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    hillshade = dem.hillshade()
    return hillshade

def calculate_aspect(dem_path, output_dir):
    """Рассчитать aspect и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    aspect = dem.aspect()
    return aspect

def calculate_curvature(dem_path, output_dir):
    """Рассчитать curvature и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    curvature = dem.curvature()
    return curvature

def calculate_planform_curvature(dem_path, output_dir):
    """Рассчитать planform curvature и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    planform_curvature = dem.planform_curvature()
    return planform_curvature

def calculate_profile_curvature(dem_path, output_dir):
    """Рассчитать profile curvature и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    profile_curvature = dem.profile_curvature()
    return profile_curvature

def calculate_surface_fit(dem_path, output_dir):
    """Рассчитать surface fit и сохранить как TIFF."""
    dem = xdem.DEM(dem_path, vcrs="EGM96")
    surface_fit = dem.surface_fit()
    return surface_fit.plot()

def calculate_fractal_roughness(dem_path, output_dir):
    """Рассчитать fractal roughness и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['fractal_roughness'], output_dir)['fractal_roughness']

def plot_terrain_attribute(attribute_array, title):
    """Plot a terrain attribute using matplotlib."""
    plt.figure(figsize=(10, 8))
    plt.imshow(attribute_array, cmap='terrain')
    plt.colorbar(label=title)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
