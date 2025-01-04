from osgeo import gdal
import rioxarray

def calculate_slope(dem_path, slope_path):
    """Рассчитать уклон на основе данных из DEM файла и вернуть как xarray DataArray."""
    gdal.DEMProcessing(
        slope_path,       # Файл с уклоном
        dem_path,         # Файл с данными о высотах
        'slope',          # Тип обработки
        computeEdges=True,
        alg='ZevenbergenThorne',
        scale=111120
    )
    print(f"Slope map created at {slope_path}")
    
    # Создаем xarray DataArray из файла
    slope_xarray = rioxarray.open_rasterio(slope_path)
    return slope_xarray
