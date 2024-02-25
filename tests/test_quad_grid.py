# test_quad_grid.py
"""
Testing script which creates sample testing polygon geometry to develop
the QuadTree Class
"""

from utilities.simple_polygon_builder import *
from utilities.quad_tree import *



# Import sample Polygon Shape & Point Data
sample_domain_gdf = generate_sample_domain()
# plot_domain(sample_domain_gdf)

polygon = sample_domain_gdf.geometry.iloc[0]
exterior_points, interior_points = PolygonShapeBuilder.extract_polygon_points(polygon)

# Calculate centroid of the polygon formed by exterior points
centroid_x = np.mean([point[0] for point in exterior_points])
centroid_y = np.mean([point[1] for point in exterior_points])
# Define width and height of the boundary based on the range of x and y coordinates of exterior points
boundary_width = max([point[0] for point in exterior_points]) - min([point[0] for point in exterior_points])
boundary_height = max([point[1] for point in exterior_points]) - min([point[1] for point in exterior_points])
# Define cx and cy as the center coordinates of the boundary
cx = centroid_x
cy = centroid_y

print(exterior_points)

exterior_points = [Point(x,y) for x, y in exterior_points]
interior_points = [Point(x,y) for x, y in interior_points]
all_points = exterior_points + interior_points

# Create the rectangle boundary using the calculated center (cx, cy), width, and height
boundary = Rectangle(Point(cx, cy), boundary_width, boundary_height)
qtree = QuadTree(boundary, capacity=1)
for point in all_points:
    qtree.insert(point)

# Plot all the points
fig = plt.figure(figsize=(14, 9))
ax = plt.subplot()

# Extract x and y coordinates from exterior points
exterior_x = [point.x for point in exterior_points]
exterior_y = [point.y for point in exterior_points]

# Extract x and y coordinates from interior points
interior_x = [point.x for point in interior_points]
interior_y = [point.y for point in interior_points]

# Scatter plot exterior points
# plt.scatter(exterior_x, exterior_y, color='blue', s=5)
# Scatter plot interior points
# plt.scatter(interior_x, interior_y, color='red', s=5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Exterior and Interior Points')

# Plot the quadtree boundaries
qtree.draw()

ax.set_aspect('equal')
plt.show()

