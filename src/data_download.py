import ee
import geemap

def initialize_gee(project: str):
    """Инициализация проекта в GEE."""
    ee.Initialize(project=project)

def download_dem(lat, lon, buffer_degrees, output_path):
    """Загрузка DEM (digital elevation model) из GEE."""
    lon1, lat1, lon2, lat2 = lon - buffer_degrees, lat - buffer_degrees, lon + buffer_degrees, lat + buffer_degrees
    region = ee.Geometry.Rectangle([lon1, lat1, lon2, lat2])
    srtm = ee.Image("USGS/SRTMGL1_003").clip(region)

    geemap.ee_export_image(
        srtm,
        filename=output_path,
        scale=30,
        region=region,
        file_per_band=False
    )
    print(f"DEM downloaded to {output_path}")
