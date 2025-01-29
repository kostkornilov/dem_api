import xdem
import rioxarray
import tempfile
import os
import matplotlib.pyplot as plt
from pyproj import CRS

def calculate_terrain_attributes(dem_path, attributes, output_dir, dst_crs="EPSG:32637", **kwargs):
    """Рассчитать несколько топографических атрибутов с использованием xdem и сохранить как TIFF файлы."""
    # Создаем DEM объект
    dem = xdem.DEM(dem_path,vcrs="WGS84")
    print(dem)
    print('1st',dem.vcrs)
    # Define the target CRS (CRS - Coordinate Reference System)
    target_crs = CRS.from_string(dst_crs)
    # Reproject DEM to the target CRS
    # ЕСЛИ НЕ СДЕЛАТЬ ПЕРЕПРОЕКЦИЮ, то считаться будет плохо
    # Перепроекция сделана на EPSG:32637 (это UTM 37N)
    # CRS выбирается в зависимости от региона
    reprojected_dem = dem.reproject(crs=target_crs, res=30)
    reprojected_dem.save(os.path.join(output_dir, "reprojected_dem.tif"))
    # Cчитаем все аттрибуты
    attribute_arrays = reprojected_dem.get_terrain_attribute(attributes, **kwargs)
    # Преобразуем Raster объекты в xarray DataArrays
    attribute_xarrays = list(map(lambda x: x.to_xarray(), attribute_arrays))

    # Сохраняем аттрибуты как GeoTIFF файлы
    for attribute, attribute_xarray in zip(attributes, attribute_xarrays):
        output_path = os.path.join(output_dir, f"{attribute}.tif")
        attribute_xarray.rio.to_raster(output_path)
    
    # Добавляем reprojected DEM в список аттрибутов (первым)
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
