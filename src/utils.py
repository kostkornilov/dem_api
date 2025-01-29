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
    """Combine multiple xarray DataArrays into a single xarray with multiple bands."""
    combined = xr.concat(xarrays, dim="band")
    combined = combined.assign_coords(band=attributes)
    return combined
