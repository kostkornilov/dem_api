import xdem
import rioxarray
import tempfile
import os
import matplotlib.pyplot as plt
def calculate_terrain_attributes(dem_path, attributes, output_dir, **kwargs):
    """Calculate multiple terrain attributes using xdem and save as TIFF files."""
    dem = xdem.DEM(dem_path)
    attribute_arrays = dem.get_terrain_attribute(attributes, **kwargs)
    attribute_files = {}
    for attribute, attribute_array in zip(attributes, attribute_arrays):
        output_path = os.path.join(output_dir, f"{attribute}.tif")
        attribute_array.save(output_path)
        # attribute_files[attribute] = output_path
    return attribute_arrays

def calculate_slope(dem_path, output_dir):
    """Рассчитать уклон и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['slope'], output_dir)['slope']
    

def calculate_hillshade(dem_path, output_dir):
    """Рассчитать hillshade и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['hillshade'], output_dir)['hillshade']

def calculate_aspect(dem_path, output_dir):
    """Рассчитать aspect и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['aspect'], output_dir)['aspect']

def calculate_curvature(dem_path, output_dir):
    """Рассчитать curvature и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['curvature'], output_dir)['curvature']

def calculate_planform_curvature(dem_path, output_dir):
    """Рассчитать planform curvature и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['planform_curvature'], output_dir)['planform_curvature']

def calculate_profile_curvature(dem_path, output_dir):
    """Рассчитать profile curvature и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['profile_curvature'], output_dir)['profile_curvature']

def calculate_maximum_curvature(dem_path, output_dir):
    """Рассчитать maximum curvature и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['maximum_curvature'], output_dir)['maximum_curvature']

def calculate_surface_fit(dem_path, output_dir):
    """Рассчитать surface fit и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['surface_fit'], output_dir)['surface_fit']

def calculate_topographic_position_index(dem_path, output_dir):
    """Рассчитать topographic position index и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['topographic_position_index'], output_dir)['topographic_position_index']

def calculate_terrain_ruggedness_index(dem_path, output_dir):
    """Рассчитать terrain ruggedness index и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['terrain_ruggedness_index'], output_dir)['terrain_ruggedness_index']

def calculate_roughness(dem_path, output_dir):
    """Рассчитать roughness и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['roughness'], output_dir)['roughness']

def calculate_rugosity(dem_path, output_dir):
    """Рассчитать rugosity и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['rugosity'], output_dir)['rugosity']

def calculate_fractal_roughness(dem_path, output_dir):
    """Рассчитать fractal roughness и сохранить как TIFF."""
    return calculate_terrain_attributes(dem_path, ['fractal_roughness'], output_dir)['fractal_roughness']

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
    
    # Test maximum curvature calculation
    maximum_curvature = calculate_maximum_curvature(dem_path, output_dir)
    print("Maximum Curvature calculated:", maximum_curvature)
    
    # # Test surface fit calculation
    # surface_fit = calculate_surface_fit(dem_path, output_dir)
    # print("Surface Fit calculated:", surface_fit)
    
    # Test topographic position index calculation
    topographic_position_index = calculate_topographic_position_index(dem_path, output_dir)
    print("Topographic Position Index calculated:", topographic_position_index)
    
    # Test terrain ruggedness index calculation
    terrain_ruggedness_index = calculate_terrain_ruggedness_index(dem_path, output_dir)
    print("Terrain Ruggedness Index calculated:", terrain_ruggedness_index)
    
    # Test roughness calculation
    roughness = calculate_roughness(dem_path, output_dir)
    print("Roughness calculated:", roughness)
    
    # Test rugosity calculation
    rugosity = calculate_rugosity(dem_path, output_dir)
    print("Rugosity calculated:", rugosity)
    
    # Test fractal roughness calculation
    fractal_roughness = calculate_fractal_roughness(dem_path, output_dir)
    print("Fractal Roughness calculated:", fractal_roughness)