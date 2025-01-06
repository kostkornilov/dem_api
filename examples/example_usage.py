from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_terrain_attributes
from src.plotting import plot_dem_and_slope_files, plot_topographical_features, plot_dem_and_feature_pairs, plot_terrain_attributes, plot_individual_attribute
from src.utils import tiff_to_xarray
import os

initialize_gee(project='projectomela')

# Определим координаты и названия файлов
lat, lon = 55.600, 37.172
buffer = 0.05
dem_file_name = "srtm.tif"
directory = "example_output"

# Загрузим DEM и получим xarray DataArray
dem_xarray = download_dem(lat, lon, buffer, dem_file_name, directory)
dem_path = os.path.join(directory, dem_file_name)

# Рассчитаем топографические атрибуты и получим пути к TIFF файлам
attributes = [
    'hillshade', 'slope', 'aspect', 'curvature', 'terrain_ruggedness_index', 'rugosity'
]
attribute_rasters = calculate_terrain_attributes(dem_path, attributes, directory)
for attribute in attribute_rasters:
    attribute.plot()
    plt.show()
attribute_files = {attr: os.path.join(directory, f"{attr}.tif") for attr in attributes}

# Преобразуем TIFF файлы в xarray DataArrays
attributes_dict = {attr: tiff_to_xarray(path) for attr, path in attribute_files.items()}

# Построим графики
# labels = ["Hillshade", "Slope (°)", "Aspect (°)", "Curvature (100 / m)", "Terrain Ruggedness Index", "Rugosity"]
# plot_terrain_attributes(dem_xarray, list(attributes_dict.values()), labels)

# Выведем статистику
def print_statistics(xarray, name):
    print(f"Statistics for {name}:")
    print(f"Mean: {xarray.mean().item()}")
    print(f"Min: {xarray.min().item()}")
    print(f"Max: {xarray.max().item()}")
    print(f"Standard Deviation: {xarray.std().item()}")
    print()

print_statistics(dem_xarray, "DEM")
for attribute, xarray in attributes_dict.items():
    print_statistics(xarray, attribute)

# Пример построения графика для отдельного атрибута
# fractal_roughness_xarray = attributes_dict['rugosity']
# plot_individual_attribute(fractal_roughness_xarray, "Rugosity", cmap="YlOrRd", cbar_title="Rugosity")