import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

# Create square polygon
square_coords = [(0, 0), (1, 0), (1, 1), (0, 1)]
square = Polygon(square_coords)

# Create circular polygon
circle_center = Point(0.5, 0.5)
radius = 0.25
circle = circle_center.buffer(radius)

# Perform the difference operation
square_with_hole = square.difference(circle)

# Create a single figure with 3 subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(3, 10))

# Plot each polygon on a separate subplot
gpd.GeoSeries(square).plot(ax=axes[0], color='cornflowerblue', edgecolor='lightgray')
axes[0].set_title('Square')
axes[0].set_aspect('equal')

gpd.GeoSeries(square).plot(ax=axes[1], color='cornflowerblue', edgecolor='lightgray')
gpd.GeoSeries(circle).plot(ax=axes[1], color='red', edgecolor='lightgray')
axes[1].set_title('Square / Circle')
axes[1].set_aspect('equal')

gpd.GeoSeries(square_with_hole).plot(ax=axes[2], color='cornflowerblue', edgecolor='lightgray')
axes[2].set_title('Square with Hole')
axes[2].set_aspect('equal')

plt.tight_layout()
plt.show()
