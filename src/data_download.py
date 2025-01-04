import ee
import geemap
import requests
import os
import shutil

def initialize_gee(project: str):
    """Инициализация проекта в GEE."""
    try:
        ee.Initialize(project=project)
        print("Google Earth Engine успешно инициализирован.")
    except ee.EEException as e:
        print(f"Ошибка инициализации: {e}")
        print("Попробуйте выполнить 'earthengine authenticate'.")

def download_dem(lat, lon, buffer_degrees, filename, directory='example_output'):
    """Загрузка DEM (digital elevation model) из GEE."""
    try:
        lon1, lat1, lon2, lat2 = lon - buffer_degrees, lat - buffer_degrees, lon + buffer_degrees, lat + buffer_degrees
        # Создание папки, если ее нет
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Временный файл в текущей рабочей директории
        temp_file = filename
        # Определение региона
        region = ee.Geometry.Rectangle([lon1, lat1, lon2, lat2])
        # Загрузка данных SRTM
        srtm = ee.Image("USGS/SRTMGL1_003").clip(region)
        # Экспорт изображения во временный файл
        geemap.ee_export_image(
            srtm,
            filename=temp_file,
            scale=30,
            region=region,
            file_per_band=False
        )
        # Перемещение временного файла в кастомную директорию
        output_path = os.path.join(directory, filename)
        shutil.move(temp_file, output_path)
        print(f"DEM downloaded to {output_path}")
        
    except Exception as e:
        print(f"Error downloading DEM: {e}")
