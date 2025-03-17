import rioxarray
import xarray as xr
import matplotlib.pyplot as plt

def create_bounding_box(lat, lon, buffer_degrees):
    """Рассчет координат области."""
    lon1 = lon - buffer_degrees
    lon2 = lon + buffer_degrees
    lat1 = lat - buffer_degrees
    lat2 = lat + buffer_degrees
    return lon1, lat1, lon2, lat2

def tiff_to_xarray(tiff_path):
    """Преобразовать TIFF файл в xarray DataArray."""
    data = rioxarray.open_rasterio(tiff_path, masked=True)
    print(f"Loaded {tiff_path}:")
    print(f"Shape: {data.shape}")
    print(f"CRS: {data.rio.crs}")
    print(f"Nodata: {data.rio.nodata}")
    print(f"Data: {data}")
    return data

def combine_xarrays(xarrays, attributes):
    """Объединить несколько xarray DataArray в один Dataset."""
    combined = xr.concat(xarrays, dim="band")
    combined = combined.assign_coords(band=attributes)
    combined = combined.rename({"y": "latitude", "x": "longitude"})
    combined_dataset = combined.to_dataset(dim="band")
    # высота (DEM) может принимать значения от -10 до 6500 метров (разрешение - 30 м)
    # уклон (slope) может принимать значения от 0 до 90 градусов
    # теневой рельеф (hillshade) может принимать значения от 0 до 255
    # Азимут (aspect) может принимать значения от 0 до 360 градусов
    # макс. отрицательное значение кривизны(curvature) (центр = -10 метров, окружающие пиксели = 6500) = -100*(4*6500-4*(-10))/900 ~= -2893.3
    # макс. положительное значение кривизны(curvature) (центр = 6500 метров, окружающие пиксели = -10) = -100*(4*(-10)-4*6500)/900 ~= 2893.3
    # макс. значение плановой кривизны (Planform curvature) и профильной кривизны (Profile curvature) точно не превывают макс. значения кривизны, т.к. описывают кривизну в определённых направлениях
    # поэтому будем считать, то Planform curvature и Profile curvature тоже могут принимать значения примерно от -3000 до 3000
    # макс. значение максимальной кривизны (Maximum curvature) = 2893.3
    # макс. значение индекса топографического положения (Topographic position index) (если центр = 6500 метров, окружающие пиксели = -10, окно = 3*3 пикселя) 
    # = 6500 - -10*8/8 = 6510, min =  -10 - 6500*8/8 = -6510
    # макc. значение индекса пересеченной местности (Terrain ruggedness index) (если центр = 6500 метров, окружающие пиксели = -10, окно = 3*3 пикселя)
    # = sqrt(8*6510**2) ~= 18413.06, min = 0
    # макс. значение шероховатости (Roughness) = 6500 - -10 = 6510, min = 0
    # макс. значение неровность поверхности (Rugosity) при заданных параметрах (rougly) = 1047.65, min = 1
    # Исходя из всех этих рассуждений, делаем вывод, что для хранения всех данных достаточно np.float16 (все значения укладываются в диапозон диапазон значений: от -65,504 до 65,504.)
    # Точность 3 знака после запятой считаем достаточной
    combined_dataset = combined_dataset.astype("float16")
    return combined_dataset
