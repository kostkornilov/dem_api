import xdem
import rioxarray
import tempfile
import os
import matplotlib.pyplot as plt
from pyproj import CRS

def calculate_terrain_attributes(dem_path, attributes, output_dir, dst_crs="EPSG:32637", **kwargs):
    """Рассчитать несколько топографических атрибутов с использованием xdem и сохранить как TIFF файлы."""
    dem = xdem.DEM(dem_path,vcrs="WGS84")
    print(dem)
    print('1st',dem.vcrs)
    # Define the target CRS
    target_crs = CRS.from_string(dst_crs)
    # Reproject DEM to the target CRS
    # ЕСЛИ НЕ СДЕЛАТЬ ПЕРЕПРОЕКЦИЮ, то считаться будет плохо
    # Перепроекция сделана на EPSG:32637
    reprojected_dem = dem.reproject(crs=target_crs, res=30)
    reprojected_dem.save(os.path.join(output_dir, "reprojected_dem.tif"))
    attribute_arrays = reprojected_dem.get_terrain_attribute(attributes, **kwargs)

    attribute_files = {}
    for attribute, attribute_array in zip(attributes, attribute_arrays):
        output_path = os.path.join(output_dir, f"{attribute}.tif")
        print(attribute_array)
        print(type(attribute_array))
        data_array = attribute_array.to_xarray()
        data_array.rio.write_crs(target_crs, inplace=True)
        data_array.rio.write_transform(attribute_array.transform, inplace=True)
        # Save as GeoTIFF
        data_array.rio.to_raster(output_path, dtype="float32", nodata=None)
        plt.figure(figsize=(10, 8))
        mappable = data_array.plot(cmap='terrain')
        plt.title(attribute)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.colorbar(mappable, label=attribute)
        plt.show()
    return attribute_arrays

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



if __name__ == "__main__":
    print("Running tests for calculations.py")
    dem_path = r"C:\Users\Asus\dem_api\example_output\srtm.tif"
    output_dir = r"C:\Users\Asus\dem_api\example_output"
    
    # Test slope calculation
    slope = calculate_slope(dem_path, output_dir)
    print("Slope calculated:", slope)
    
    # Test hillshade calculation
    hillshade = calculate_hillshade(dem_path, output_dir)
    print("Hillshade calculated:", hillshade)
    
    # Test aspect calculation
    aspect = calculate_aspect(dem_path, output_dir)
    print("Aspect calculated:", aspect)
    
    # Test curvature calculation
    curvature = calculate_curvature(dem_path, output_dir)
    print("Curvature calculated:", curvature)
    
    # Test planform curvature calculation
    planform_curvature = calculate_planform_curvature(dem_path, output_dir)
    print("Planform Curvature calculated:", planform_curvature)
    
    # Test profile curvature calculation
    profile_curvature = calculate_profile_curvature(dem_path, output_dir)
    print("Profile Curvature calculated:", profile_curvature)
    
    # Test fractal roughness calculation
    fractal_roughness = calculate_fractal_roughness(dem_path, output_dir)
    print("Fractal Roughness calculated:", fractal_roughness)