import matplotlib.pyplot as plt
import rioxarray
import xdem
import math

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


def plot_individual_attribute(attribute_xarray, title, cmap="viridis", cbar_title=""):
    """Построить график для отдельного атрибута (xarray)"""
    plt.figure(figsize=(10, 8))
    mappable = attribute_xarray.plot(cmap=cmap)
    plt.title(title)
    plt.colorbar(mappable, label=cbar_title)
    plt.show()

def plot_attributes(attributes, attribute_rasters, dem_path):
    """Графики из Raster объектов."""
    # Создаем DEM объект (из tif файла)
    dem = xdem.DEM(dem_path)
    # кол-во графиков
    n_attributes = len(attributes) 
    # кол-во столбцов на графике
    n_cols = 2
    # кол-во строк на графике
    n_rows = math.ceil(n_attributes / n_cols)
    for i in range(n_attributes):
        plt.figure(figsize=(10, 8))
        attribute_rasters[i].plot(cmap="viridis")
        plt.title(attributes[i])
        plt.xticks([])
        plt.yticks([])
        plt.show()

if __name__ == "__main__":
    # Example attributes and corresponding rasters
    attributes = ["DEM", "Slope", "Aspect", "Curvature", "Hillshade", "Roughness"]
    
    # Example paths to attribute rasters
    attribute_raster_paths = [
        "example_output/reprojected_dem.tif",
        "example_output/slope.tif",
        "example_output/aspect.tif",
        "example_output/curvature.tif",
        "example_output/hillshade.tif",
        "example_output/roughness.tif"
    ]
    
    # Load attribute rasters using rioxarray
    attribute_rasters = [xdem.DEM(path) for path in attribute_raster_paths]
    # PROBLEM: открывается только DEM, через rioxarray открывается хрень пустая
    
    # Path to DEM file
    dem_path = "example_output/reprojected_dem.tif"
    
    # Call the function to plot attributes
    plot_attributes(attributes, attribute_rasters, dem_path)
#     print(6\%6)