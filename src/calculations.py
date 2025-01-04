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

def calculate_hillshade(dem_path, hillshade_path):
    """hillshade -- это просто тень, которую создает солнце на поверхности. Нужен для визуализации.
    Возсожно, магическим образом будет полезно для ml моделей."""
    gdal.DEMProcessing(
        hillshade_path,
        dem_path,
        'hillshade',
        computeEdges=True,
        alg='ZevenbergenThorne',
        scale=111120
    )
    print(f"Hillshade map created at {hillshade_path}")
    hillshade_xarray = rioxarray.open_rasterio(hillshade_path)
    return hillshade_xarray

def calculate_aspect(dem_path, aspect_path):
    """Aspect -- это направление склона. Это угол между направлением на север и направлением на склон."""
    gdal.DEMProcessing(
        aspect_path,
        dem_path,
        'aspect',
        computeEdges=True,
        alg='ZevenbergenThorne'
    )
    print(f"Aspect map created at {aspect_path}")
    aspect_xarray = rioxarray.open_rasterio(aspect_path)
    return aspect_xarray

def calculate_tri(dem_path, tri_path):
    """TRI -- это триангуляционная неровность поверхности."""
    gdal.DEMProcessing(
        tri_path,
        dem_path,
        'TRI',
        computeEdges=True
    )
    print(f"TRI map created at {tri_path}")
    tri_xarray = rioxarray.open_rasterio(tri_path)
    return tri_xarray

def calculate_tpi(dem_path, tpi_path):
    """TPI -- это разница между высотой точки и средней высотой в окрестности точки."""
    gdal.DEMProcessing(
        tpi_path,
        dem_path,
        'TPI',
        computeEdges=True
    )
    print(f"TPI map created at {tpi_path}")
    tpi_xarray = rioxarray.open_rasterio(tpi_path)
    return tpi_xarray

def calculate_roughness(dem_path, roughness_path):
    """Roughness -- это разница между максимальным и минимальным уровнем высот в окрестности точки."""
    gdal.DEMProcessing(
        roughness_path,
        dem_path,
        'roughness',
        computeEdges=True
    )
    print(f"Roughness map created at {roughness_path}")
    roughness_xarray = rioxarray.open_rasterio(roughness_path)
    return roughness_xarray

