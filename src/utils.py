def create_bounding_box(lat, lon, buffer_degrees):
    """Рассчет координат области."""
    lon1 = lon - buffer_degrees
    lon2 = lon + buffer_degrees
    lat1 = lat - buffer_degrees
    lat2 = lat + buffer_degrees
    return lon1, lat1, lon2, lat2
