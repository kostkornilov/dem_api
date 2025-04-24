from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_terrain_attributes
from src.plotting import plot_all_bands
import os
from pathlib import Path

def run(geo_json_path, output_directory='example_output'):
    """
    Основная функция для запуска всего процесса.
    
    Принимает путь к GeoJSON файлу и директорию для сохранения выходных данных.
    """
    # Инициализируем GEE
    initialize_gee(project='projectomela')

    # Определим координаты и названия файлов
    geojson_path = str(geo_json_path)
    dem_file_name = "srtm.tif"
    directory = "example_output"

    # Загрузим DEM из GEE (DEM сохранится в .tiff файл в директории directory)
    dem_xarray = download_dem(geojson_path, dem_file_name, directory)
    # Путь к DEM файлу
    dem_path = os.path.join(directory, dem_file_name)
    attributes = [
    'slope', 'hillshade', 'aspect', 'curvature', 'planform_curvature', 'profile_curvature',
    'maximum_curvature', 'topographic_position_index', 'terrain_ruggedness_index',
    'roughness', 'rugosity']

    # Получаем объект xarray.Dataset
    terrain_dataset = calculate_terrain_attributes(dem_path, attributes, directory)

    return terrain_dataset

if __name__ == "__main__":
    # Путь к GeoJSON файлу
    geo_json_path = "examples/sample.geojson"
    # Запускаем основную функцию
    terrain_dataset = run(geo_json_path)
    print(terrain_dataset)
