# path_planner.py

"""


"""

from utilities.shapefile_handler import ShapefileHandler



# Test / Example Useage
shapefile_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
)

chart_us4ma23m = ShapefileHandler(shapefile_path)
df_land_coordinates = chart_us4ma23m.get_land_coordinates()
print(df_land_coordinates.head())

centroids = chart_us4ma23m.calculate_polygon_centroids()
# chart_us4ma23m.plot_land_coordinates(plot_centroids=True)
#
print(len(centroids))
print(type(centroids))



water_polygon = chart_us4ma23m.get_water_polygon()
# print(chart_us4ma23m.data['geometry'])
# print(water_polygon)
# print(len(water_polygons))
# chart_us4ma23m.plot_water_polygons(water_polygon)

