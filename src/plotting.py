import matplotlib.pyplot as plt
import rioxarray

def plot_dem_and_slope_files(dem_xarray, slope_xarray):
    """Построить графики для DEM и уклона на одном графике."""
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    
    # Plot DEM
    dem_xarray.plot(ax=axes[0])
    axes[0].set_title('Digital Elevation Model (DEM)')
    
    # Plot Slope
    slope_xarray.plot(ax=axes[1])
    axes[1].set_title('Slope')
    
    plt.show()