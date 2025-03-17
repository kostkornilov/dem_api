from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_terrain_attributes
from src.plotting import plot_all_bands, plot_individual_attribute
from src.utils import tiff_to_xarray, combine_xarrays
import os

# Инициализируем GEE
initialize_gee(project='projectomela')

# Определим координаты и названия файлов
geo_json_path = "example_input/area.geojson"
dem_file_name = "srtm.tif"
directory = "example_output"

# Загрузим DEM из GEE (DEM сохранится в tiff файл в директории directory)
dem_dataset = download_dem(geo_json_path, dem_file_name, directory)
# Путь к DEM файлу
dem_path = os.path.join(directory, dem_file_name)

# Определим, какие аттрибуты мы хотим считать
attributes = [
    'slope', 'hillshade', 'aspect', 'curvature', 'planform_curvature', 'profile_curvature',
    'maximum_curvature', 'topographic_position_index', 'terrain_ruggedness_index',
    'roughness', 'rugosity'
]

# Получаем список из len(attributes) + 1 объектов Xarray; также сохраняем их как GeoTIFF файлы
attribute_xarrays = calculate_terrain_attributes(dem_path, attributes, directory)

# Пример преобразования TIFF файлов в xarray DataArrays
# attribute_files = {attr: os.path.join(directory, f"{attr}.tif") for attr in attributes}
# xarrays = [tiff_to_xarray(path) for path in attribute_files.values()]
# Объединим xarray DataArrays в один xarray с несколькими каналами
combined_xarray = combine_xarrays(attribute_xarrays, attributes)
# Добавляем измерение времени
combined_xarray = combined_xarray.expand_dims(time=dem_dataset.time)

# Вывод каждого канала на отдельном графике
plot_all_bands(combined_xarray)