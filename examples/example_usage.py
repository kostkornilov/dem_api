from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_terrain_attributes
from src.plotting import plot_attributes, plot_dem_and_slope_files, plot_topographical_features, plot_dem_and_feature_pairs, plot_individual_attribute
from src.utils import tiff_to_xarray, combine_xarrays
import os

# Инициализируем GEE
initialize_gee(project='projectomela')

# Определим координаты и названия файлов
lat, lon = 55.600, 37.172
buffer = 0.1
dem_file_name = "srtm.tif"
directory = "example_output"

# Загрузим DEM и получим xarray DataArray
dem_xarray = download_dem(lat, lon, buffer, dem_file_name, directory)
dem_path = os.path.join(directory, dem_file_name)

# Рассчитаем топографические атрибуты и получим пути к TIFF файлам
attributes = [
    'slope', 'hillshade', 'aspect', 'curvature', 'planform_curvature', 'profile_curvature',
    'maximum_curvature', 'topographic_position_index', 'terrain_ruggedness_index',
    'roughness', 'rugosity'
]

# Получаем объекты Raster для каждого показателя
attribute_rasters = calculate_terrain_attributes(dem_path, attributes, directory)
# Построим графики для Ratser объектов
# plot_attributes(attributes, attribute_rasters, dem_path)
# Преобразуем TIFF файлы в xarray DataArrays
attribute_files = {attr: os.path.join(directory, f"{attr}.tif") for attr in attributes}
xarrays = [tiff_to_xarray(path) for path in attribute_files.values()]
# Объединим xarray DataArrays в один xarray с несколькими каналами
combined_xarray = combine_xarrays(xarrays, attributes)
# Информацию
def print_statistics(xarray, name):
    print(f"Statistics for {name}:")
    print(f"xarray: {xarray}")
    print()

print_statistics(dem_xarray, "DEM")
for attribute in attributes:
    print_statistics(combined_xarray.sel(band=attribute), attribute)

# Пример построения графика для отдельного атрибута
fractal_roughness_xarray = combined_xarray.sel(band='slope')
plot_individual_attribute(fractal_roughness_xarray, "Rugosity", cmap="YlOrRd", cbar_title="Rugosity")