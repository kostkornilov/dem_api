import rasterio
from rasterio.plot import show
from examples.example_usage import dem_path, slope_path
import matplotlib.pyplot as plt

def plot_tif_files(srtm_path, slope_path):
    # Open the SRTM file
    with rasterio.open(srtm_path) as srtm_src:
        srtm_data = srtm_src.read(1)
    
    # Open the slope file
    with rasterio.open(slope_path) as slope_src:
        slope_data = slope_src.read(1)
    
    # Plot the SRTM and slope data side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot SRTM data
    ax1.set_title('SRTM')
    show(srtm_data, ax=ax1, cmap='terrain')
    
    # Plot slope data
    ax2.set_title('Slope')
    show(slope_data, ax=ax2, cmap='viridis')
    
    plt.tight_layout()
    plt.show()

# Example usage
plot_tif_files(dem_path, slope_path)