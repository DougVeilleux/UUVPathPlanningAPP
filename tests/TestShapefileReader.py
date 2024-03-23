#test_shp_handler.py

from utilities.ShapefileHandler import ShapefileHandler



# Test / Example Useage
shapefile_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/SHAPE_FILE/US4MA43M/US4MA43M_SHAPEFILE.shp'
)

chart_us4ma23m = ShapefileHandler(shapefile_path)
df_land_coordinates = chart_us4ma43m.get_land_coordinates()
print(df_land_coordinates.head())

chart_us4ma23m.plot_land_coordinates()
# chart_us4ma23m.plot_shapefile_with_df()
