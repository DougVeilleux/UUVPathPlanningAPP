import math
import matplotlib.pyplot as plt


# def get_neighbors_astar(current_point, distance=500, number_of_neighbors=8):
#     """
#     Calculate the neighboring points of the current point.
#     :param current_point: current GPS coordinate for which neighbors are found
#     :param distance: Distance from the point (in meters) to find neighbors.
#     :param number_of_neighbors: number of neighbors
#     :return: neighbors: list of GPS coordinates of the current point.
#     """
#     # Define the lat / lon
#     longitude, latitude = current_point[0], current_point[1]
#
#     # Calculate the angle between each neighbor
#     angle_increment = 360 / number_of_neighbors
#
#     # Calculate the neighbors coordinates
#     neighbors = []
#     for i in range(number_of_neighbors):
#         angle = math.radians(angle_increment * i)
#         dx = distance * math.cos(angle)
#         dy = distance * math.sin(angle)
#         neighbor = (longitude + dx, latitude + dy)
#         neighbors.append(neighbor)
#
#     return neighbors
#
# # Example usage:
# current_point = (-70.80, 41.30)
# d = 0.009  # Distance in meters
# num_neighbors = 16
# neighbors = get_neighbors_astar(current_point, distance=d, number_of_neighbors=num_neighbors)
# print(neighbors)
#
# # Extract longitude and latitude
# lon, lat = current_point[0], current_point[1]
# lons, lats = zip(*neighbors)
#
# # Plotting
# plt.figure(figsize=(10, 10))
# plt.plot(lon, lat, 'bo', label='Original Point')
# plt.plot(lons, lats, 'ro', label='Neighbors', linestyle='None', marker='o')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('GPS Coordinates and Neighbors')
# plt.legend()
# plt.grid(True)
# # Set x and y-axis limits
# plt.xlim(lon - .01, lon + .01)  # Set x-axis limits to be 2.0 degrees around the original longitude
# plt.ylim(lat - .01, lat + .01)  # Set y-axis limits to be 2.0 degrees around the original latitude
# # Set equal aspect ratio
# # Set equal aspect ratio
# plt.gca().set_aspect('equal', adjustable='box')
#
# plt.show()




def get_neighbors_square(current_point, distance=500):
    """
    Calculate the neighboring points forming a square around the current point.
    :param current_point: current GPS coordinate for which neighbors are found
    :param distance: Distance from the point (in meters) to find neighbors.
    :return: neighbors: list of GPS coordinates of the current point.
    """
    # Define the lat / lon
    longitude, latitude = current_point[0], current_point[1]

    # Calculate half distance for the corner nodes
    half_distance = distance / 2

    # Calculate the neighbors coordinates forming a square
    neighbors = []

    # Corners
    neighbors.append((longitude - half_distance, latitude - half_distance))  # Lower-left corner
    neighbors.append((longitude + half_distance, latitude - half_distance))  # Lower-right corner
    neighbors.append((longitude + half_distance, latitude + half_distance))  # Upper-right corner
    neighbors.append((longitude - half_distance, latitude + half_distance))  # Upper-left corner

    # Middle of each leg
    neighbors.append((longitude, latitude - half_distance))  # Middle of lower leg
    neighbors.append((longitude + half_distance, latitude))  # Middle of right leg
    neighbors.append((longitude, latitude + half_distance))  # Middle of upper leg
    neighbors.append((longitude - half_distance, latitude))  # Middle of left leg

    return neighbors

def plot_neighbors(current_point, neighbors):
    # Extract longitude and latitude
    lon, lat = current_point[0], current_point[1]
    lons, lats = zip(*neighbors)

    # Plotting
    plt.figure(figsize=(10, 10))
    plt.plot(lon, lat, 'bo', label='Original Point')
    plt.plot(lons, lats, 'ro', label='Neighbors', linestyle='None', marker='o')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('GPS Coordinates and Neighbors')
    plt.legend()
    plt.grid(True)
    # Set equal aspect ratio
    plt.axis('equal')
    plt.show()

# Example usage:

current_point = (-70.80, 41.30)
distance = 1000  # Distance in meters
neighbors = get_neighbors_square(current_point, distance)
print(neighbors)

# Plotting
plot_neighbors(current_point, neighbors)























