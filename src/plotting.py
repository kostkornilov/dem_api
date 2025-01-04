import matplotlib.pyplot as plt
import rioxarray

def plot_dem_and_slope_files(dem_xarray, slope_xarray):
    """Построить графики для DEM и уклона на одном графике."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot DEM
    dem_xarray.plot(ax=axes[0], cmap='terrain')
    axes[0].set_title('Digital Elevation Model (DEM)')
    
    # Plot Slope
    slope_xarray.plot(ax=axes[1])
    axes[1].set_title('Slope')
    
    plt.show()

def plot_topographical_features(features_dict):
    """Построить графики для различных топографических характеристик."""
    num_features = len(features_dict)
    fig, axes = plt.subplots(1, num_features, figsize=(6 * num_features, 6))
    
    for i, (title, xarray) in enumerate(features_dict.items()):
        xarray.plot(ax=axes[i])
        axes[i].set_title(title)
    
    plt.tight_layout(pad=3.0)
    plt.show()

def plot_dem_and_feature_pairs(dem_xarray, features_dict):
    """Построить отдельные графики для каждой пары DEM и топографической характеристики."""
    for title, xarray in features_dict.items():
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        
        # Plot DEM
        dem_xarray.plot(ax=axes[0], cmap='terrain')
        axes[0].set_title('Digital Elevation Model (DEM)')
        
        # Plot Feature
        xarray.plot(ax=axes[1])
        axes[1].set_title(title)
        
        plt.tight_layout(pad=3.0)
        plt.show()