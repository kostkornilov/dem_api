from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_slope

initialize_gee(project='projectomela')

# Определим координаты и пути к файлам
lat, lon = 55.600, 37.172
buffer = 0.05
dem_path = "example_output/srtm.tif"
slope_path = "example_output/slope.tif"

# Загрузим DEM
download_dem(lat, lon, buffer, dem_path)

# Рассчитаем уклон
calculate_slope(dem_path, slope_path)
