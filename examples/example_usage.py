from src.data_download import initialize_gee, download_dem
from src.calculations import calculate_slope

initialize_gee(project='projectomela')

# Определим координаты и названия файлов
lat, lon = 55.600, 37.172
buffer = 0.05
dem_path = "srtm.tif"
slope_path = "slope.tif"

# Загрузим DEM
download_dem(lat, lon, buffer, dem_path)

# Рассчитаем уклон
calculate_slope(dem_path, slope_path)
