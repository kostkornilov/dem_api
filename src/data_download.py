import ee
import geemap
import json
import os
import shutil
import rioxarray
import xarray as xr

def initialize_gee(project: str):
    """Инициализация проекта в GEE."""
    try:
        ee.Initialize(project=project)
        print("Google Earth Engine успешно инициализирован.")
    except ee.EEException as e:
        print(f"Ошибка инициализации: {e}")
        print("Попробуйте выполнить 'earthengine authenticate'.")

def download_dem(geo_json_path, filename, directory='example_output'):
    """
    Загрузка DEM (digital elevation model) из GEE и возврат как xarray DataArray.
    
    Принимает путь к GeoJSON файлу. Из файла извлекаются координаты из первой Feature.
    Если тип геометрии Point, скачивается значение только для точки.
    Если тип геометрии Polygon, вычисляется ограничивающий прямоугольник.
    """
    try:
        # Чтение GeoJSON файла
        with open(geo_json_path, "r", encoding="utf-8") as f:
            geojson_data = json.load(f)
        
        feature = geojson_data["features"][0]
        geometry = feature["geometry"]
        geom_type = geometry["type"]
        time = feature["properties"].get("time", "unknown")
        
        # Загрузка данных SRTM
        srtm = ee.Image("USGS/SRTMGL1_003")
        
        if geom_type == "Point":
            lon, lat = geometry["coordinates"]
            point = ee.Geometry.Point(lon, lat)
            # Получение значения DEM для точки
            sample = srtm.sample(region=point, scale=30).first()
            if sample is None:
                raise ValueError("Не удалось получить значение DEM для точки.")
            dem_value = sample.get('elevation').getInfo()
            # Создаем xarray DataArray с единственным значением
            dem_xarray = xr.DataArray(
                [[dem_value]],
                dims=["y", "x"],
                coords={"y": [lat], "x": [lon]}
            )
            print(f"DEM value at point ({lon}, {lat}): {dem_value}")
            return dem_xarray
        
        elif geom_type == "Polygon":
            # Берем координаты внешнего кольца (первый элемент списка)
            coords = geometry["coordinates"][0]
            lons = [pt[0] for pt in coords]
            lats = [pt[1] for pt in coords]
            lon1, lat1, lon2, lat2 = min(lons), min(lats), max(lons), max(lats)
            
            # Создание папки, если её нет
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Определение региона на основе вычисленных координат
            region = ee.Geometry.Rectangle([lon1, lat1, lon2, lat2])
            
            # Обрезка SRTM по региону
            srtm_clipped = srtm.clip(region)
            
            # Временный файл в текущей рабочей директории
            temp_file = filename
            
            # Экспорт изображения во временный файл
            geemap.ee_export_image(
                srtm_clipped,
                filename=temp_file,
                scale=30,
                region=region,
                file_per_band=False
            )
            
            # Перемещение временного файла в указанную директорию
            output_path = os.path.join(directory, filename)
            shutil.move(temp_file, output_path)
            print(f"DEM downloaded to {output_path}")
            
            # Загрузка DEM как xarray DataArray
            dem_xarray = rioxarray.open_rasterio(output_path)
            return dem_xarray
        
        else:
            raise ValueError(f"Unsupported geometry type: {geom_type}")
        
    except Exception as e:
        print(f"Error downloading DEM: {e}")
        return None
