import ee
import geemap
import requests

def initialize_gee(project: str):
    """Инициализация проекта в GEE."""
    try:
        ee.Initialize(project=project)
        print("Google Earth Engine успешно инициализирован.")
    except ee.EEException as e:
        print(f"Ошибка инициализации: {e}")
        print("Попробуйте выполнить 'earthengine authenticate'.")

def download_dem(lat, lon, buffer_degrees, output_path):
    """Загрузка DEM (digital elevation model) из GEE."""
    lon1, lat1, lon2, lat2 = lon - buffer_degrees, lat - buffer_degrees, lon + buffer_degrees, lat + buffer_degrees
    region = ee.Geometry.Rectangle([lon1, lat1, lon2, lat2])
    srtm = ee.Image("USGS/SRTMGL1_003").clip(region)
    print("Геометрия области:", region.getInfo())
    print("Проверка данных SRTM:", srtm.getInfo())
    try:
        geemap.ee_export_image(
            srtm,
            filename=output_path,
            scale=30,
            region=region,
            file_per_band=False
        )
        print(f"DEM downloaded to {output_path}")
    except requests.exceptions.JSONDecodeError as e:
        # судя по всему в GEE есть лимит на размер данных, который превышен. Поэтому сервер как-то странно отвечает
        # надо разобраться, как этой ошибки избежать. Судя по всему она возникает при повторном запросе
        print("Failed to decode JSON response:", e)
    except Exception as e:
        print("An error occurred:", e)
