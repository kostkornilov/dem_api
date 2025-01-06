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

def plot_terrain_attributes(dem, attributes, labels):
    """Построить графики для результатов выполнения get_terrain_attributes."""
    num_attributes = len(attributes)
    rows = (num_attributes + 1) // 2
    plt.figure(figsize=(12, 6 * rows))
    plt_extent = [dem.bounds.left, dem.bounds.right, dem.bounds.bottom, dem.bounds.top]

    cmaps = ["Greys_r", "Reds", "twilight", "RdGy_r", "Purples", "YlOrRd"]
    vlims = [(None, None) for _ in range(num_attributes)]
    if num_attributes > 3:
        vlims[3] = [-2, 2]

    for i in range(num_attributes):
        plt.subplot(rows, 2, i + 1)
        plt.imshow(attributes[i].squeeze(), cmap=cmaps[i % len(cmaps)], extent=plt_extent, vmin=vlims[i][0], vmax=vlims[i][1])
        cbar = plt.colorbar()
        cbar.set_label(labels[i])
        plt.xticks([])
        plt.yticks([])

    plt.tight_layout()
    plt.show()

def plot_individual_attribute(attribute_xarray, title, cmap="viridis", cbar_title=""):
    """Построить график для отдельного атрибута."""
    attribute_xarray.plot(cmap=cmap)
    plt.title(title)
    plt.colorbar(label=cbar_title)
    plt.show()

def plot_attribute(dem):
    pass