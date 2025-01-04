from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_slope
from src.plotting import plot_dem_and_slope_files
import os

initialize_gee(project='projectomela')

# Определим координаты и названия файлов
lat, lon = 55.600, 37.172
buffer = 0.05
dem_file_name = "srtm.tif"
slope_file_name = "slope.tif"
directory = "example_output"

# Загрузим DEM и получим xarray DataArray
dem_xarray = download_dem(lat, lon, buffer, dem_file_name, directory)
dem_path = os.path.join(directory, dem_file_name)
slope_path = os.path.join(directory, slope_file_name)

# Рассчитаем уклон и получим xarray DataArray
slope_xarray = calculate_slope(dem_path, slope_path)
# xarry можно сохранить в файл. Но это будет либо GeoTIFF, либо NetCDF, либо Zarr

# Построим графики
plot_dem_and_slope_files(dem_xarray, slope_xarray)

# Выведем xarray DataArray
print(dem_xarray)
print(slope_xarray)
