from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_slope, calculate_hillshade, calculate_aspect, calculate_tri, calculate_tpi, calculate_roughness
from src.plotting import plot_dem_and_slope_files, plot_topographical_features, plot_dem_and_feature_pairs
import os

initialize_gee(project='projectomela')

# Определим координаты и названия файлов
lat, lon = 55.600, 37.172
buffer = 0.05
dem_file_name = "srtm.tif"
slope_file_name = "slope.tif"
hillshade_file_name = "hillshade.tif"
aspect_file_name = "aspect.tif"
tri_file_name = "tri.tif"
tpi_file_name = "tpi.tif"
roughness_file_name = "roughness.tif"
directory = "example_output"

# Загрузим DEM и получим xarray DataArray
dem_xarray = download_dem(lat, lon, buffer, dem_file_name, directory)
dem_path = os.path.join(directory, dem_file_name)
slope_path = os.path.join(directory, slope_file_name)

# Рассчитаем уклон и получим xarray DataArray
slope_xarray = calculate_slope(dem_path, slope_path)
# xarry можно сохранить в файл. Но это будет либо GeoTIFF, либо NetCDF, либо Zarr

hillshade_xarray = calculate_hillshade(dem_path, os.path.join(directory, hillshade_file_name))
aspect_xarray = calculate_aspect(dem_path, os.path.join(directory, aspect_file_name))

# color_relief_xarray = calculate_color_relief(dem_path, os.path.join(directory, color_relief_file_name), color_file)
# Закомментировання штука тоже нужна только для визуализации. Там на вход подается файл с цветами, и на выходе получается карта цветов. Подумал, что не нужна.

tri_xarray = calculate_tri(dem_path, os.path.join(directory, tri_file_name))
tpi_xarray = calculate_tpi(dem_path, os.path.join(directory, tpi_file_name))
roughness_xarray = calculate_roughness(dem_path, os.path.join(directory, roughness_file_name))



# Построим графики
features_dict = {
    'Slope': slope_xarray,
    'Hillshade': hillshade_xarray,
    'Aspect': aspect_xarray,
    # 'Color Relief': color_relief_xarray,
    'TRI': tri_xarray,
    'TPI': tpi_xarray,
    'Roughness': roughness_xarray
}
plot_dem_and_feature_pairs(dem_xarray, features_dict)

# Выведем статистику
def print_statistics(xarray, name):
    print(f"Statistics for {name}:")
    print(f"Mean: {xarray.mean().item()}")
    print(f"Min: {xarray.min().item()}")
    print(f"Max: {xarray.max().item()}")
    print(f"Standard Deviation: {xarray.std().item()}")
    print()

print_statistics(dem_xarray, "DEM")
print_statistics(slope_xarray, "Slope")
print_statistics(tpi_xarray, "TPI")
print_statistics(roughness_xarray, "Roughness")
print_statistics(tri_xarray, "TRI")
print_statistics(hillshade_xarray, "Hillshade")
print_statistics(aspect_xarray, "Aspect")