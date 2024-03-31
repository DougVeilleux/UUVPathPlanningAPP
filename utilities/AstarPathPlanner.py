# AstarPathPlanner.py

import math
import heapq
import time

from utilities.QuadTreeGeodata import *


class AStarPathPlanner:
    """
    This class contains the methods needed to generate a path plan from a start point
        and end up at a goal point.  These points given as a GPS coordinate.
    """

    def __init__(self, quadtree):
        """ Initialize the path planning object. """
        self.quadtree = quadtree
        self.fig, self.ax = plt.subplots(figsize=(14, 9))  # Create figure and axis here


    def astar_path(self, start_point, goal_point, distance=500, number_of_neighbors=4):
        """
        A Star path planning algorithm
        :param start_point: the start point with coordinates longitude, latitude
        :param goal_point: the goal node with coordinates longitude, latitude, and landOrWater value
        :return: path: list of coordinates defining the optimal A star path.
        """

        start_point_longitude, start_point_latitude = start_point[0], start_point[1]
        goal_point_longitude, goal_point_latitude = goal_point[0], goal_point[1]
        decimal_distance = self.meters_to_decimal_degrees(start_point, distance)
        open_set = [(0, start_point)]
        came_from = {}
        g_score = {start_point: 0}
        f_score = {start_point: self.h_euclidean(start_point, goal_point)}
        visited = set()

        past_points_for_display = []
        display_count = 0
        visited_count = {}  # Dictionary to store the number of times each node has been visited

        while open_set:
            # Get node with the lowest f_score value from the open set and set to current node
            _, current = heapq.heappop(open_set)
            if current in visited: # Check if visited node and continue if True
                continue
            visited.add(current)
            visited_count[current] = visited_count.get(current, 0) + 1
            # Debug statements to print visited set and visited count
            if visited_count[current] > 1:
                print("\nVisited Set:", visited)
                print("Visited Count:", visited_count)

            display_count += 1
            if display_count % 20 == 0:
                print("AStar Searching...loop number: ", display_count) # Debug Statement

            # Debug Visualization Elements
            past_points_for_display.append(current)
            self.visualize_astar_algorithm(start_point, goal_point, current, past_points_for_display)


            # Check if goal has been found and return the path
            if self.h_euclidean(current, goal_point) <= 0.015:
                print("Goal Point Reached!") # Debug Statement
                return self.reconstruct_path(came_from, current, goal_point)

            # neighbors = self.get_neighbors_astar_radial(current, distance=decimal_distance, number_of_neighbors=number_of_neighbors)
            neighbors = self.get_neighbors_astar_square(current, distance=decimal_distance)
            # print("Found land? ", found_land)
            for neighbor in neighbors:

                if neighbor[2] == 1:
                    # Penalize the neighbor heavily so it's less likely to be selected
                    heuristic = float('inf')  # Set heuristic to infinity
                else:
                    # Calculate the Euclidean distance heuristic as normal
                    heuristic = self.h_euclidean(neighbor, goal_point, visited_count)

                tentative_g_score = g_score.get(current, float('inf')) + self.h_euclidean(current, neighbor, visited_count)
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    # print("Came From: ", came_from)
                    g_score[neighbor] = tentative_g_score  # Update the g_score of the neighbor node
                    f_score = tentative_g_score + heuristic
                    if neighbor not in open_set:
                        heapq.heappush(open_set, (f_score, neighbor))

        return None  # Failed to find a path

    def reconstruct_path(self, came_from, current, goal_point):
        """
        Construct the Astar optimized path
        :param came_from: store the parent point of the path
        :param current: current point
        :return: total_path: the path in the correct order from start point to goal point
        """
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current)
        # Append the goal_point to the end of the path
        goal_point = (*goal_point, 0) if len(goal_point) == 2 else goal_point
        total_path.append(goal_point)
        # Extract longitude and latitude from each path in total_path
        path = [(lon, lat) for lon, lat, *_ in total_path]
        return path[::-1]


    #vvvvv HELPER METHODS vvvvv

    def meters_to_decimal_degrees(self, current_point, distance_meters):
        # Radius of the Earth in meters
        earth_radius_meters = 6371000.0

        # Convert latitude from degrees to radians
        lat_rad = math.radians(current_point[1])

        # Calculate the circumference of the Earth at the given latitude
        circumference_at_lat = 2 * math.pi * earth_radius_meters * math.cos(lat_rad)

        # Convert the distance in meters to decimal degrees
        decimal_degrees = (distance_meters / circumference_at_lat) * 360.0

        return decimal_degrees

    def calculate_heading(self, start_point, goal_point):
        """
        Calculate the heading angle (in degrees) from the start_point to the goal_point.
        :param start_point: Starting GPS coordinate (longitude, latitude).
        :param goal_point: Goal GPS coordinate (longitude, latitude).
        :return: Heading angle in degrees.
        """
        # Extract longitude and latitude values
        start_lon, start_lat = start_point[0], start_point[1]
        goal_lon, goal_lat = goal_point[0], goal_point[1]

        # Calculate the differences in longitude and latitude
        delta_lon = math.radians(goal_lon - start_lon)
        start_lat = math.radians(start_lat)
        goal_lat = math.radians(goal_lat)

        # Calculate x and y components of the direction vector
        y = math.sin(delta_lon) * math.cos(goal_lat)
        x = math.cos(start_lat) * math.sin(goal_lat) - \
            math.sin(start_lat) * math.cos(goal_lat) * math.cos(delta_lon)

        # Calculate the angle in radians
        angle_rad = math.atan2(y, x)

        # Convert angle from radians to degrees
        angle_deg = math.degrees(angle_rad)

        # Ensure the angle is within the range [0, 360)
        if angle_deg < 0:
            angle_deg += 360

        return angle_deg

    # def calculate_new_position(self, current_point, heading, distance_to_new_point):
    #     """
    #     Calculate the new position based on the current position, heading, and distance.
    #     :param current_point: Tuple (longitude, latitude) representing the current position.
    #     :param heading: Heading angle in degrees (clockwise from north).
    #     :param distance_to_new_point: Distance to the new point in meters.
    #     :return: Tuple (longitude, latitude) representing the new position.
    #     """
    #     # Extract latitude and longitude values of the current point
    #     current_lon, current_lat = current_point[0], current_point[1]
    #
    #     # Convert heading from degrees to radians
    #     heading_rad = math.radians(heading)
    #
    #     # Radius of the Earth in meters
    #     R = 6371000
    #
    #     # Convert latitude and longitude from degrees to radians
    #     current_lat_rad = math.radians(current_lat)
    #     current_lon_rad = math.radians(current_lon)
    #
    #     # Calculate the new latitude and longitude
    #     new_lat = math.asin(math.sin(current_lat_rad) * math.cos(distance_to_new_point / R) +
    #                         math.cos(current_lat_rad) * math.sin(distance_to_new_point / R) *
    #                         math.cos(heading_rad))
    #
    #     new_lon = current_lon_rad + math.atan2(math.sin(heading_rad) * math.sin(distance_to_new_point / R) *
    #                                            math.cos(current_lat_rad),
    #                                            math.cos(distance_to_new_point / R) -
    #                                            math.sin(current_lat_rad) * math.sin(new_lat))
    #
    #     # Convert new latitude and longitude from radians to degrees
    #     new_lat_deg = math.degrees(new_lat)
    #     new_lon_deg = math.degrees(new_lon)
    #
    #     return new_lon_deg, new_lat_deg

    def get_neighbors_astar_radial(self, current_point, distance=500, number_of_neighbors=8):
        """
        Calculate the neighboring points of the current point.
        :param current_point: current GPS coordinate for which neighbors are found
        :param distance: Distance from the point (in meters) to find neighbors.
        :param number_of_neighbors: number of neighbors
        :return: neighbors: list of GPS coordinates of the current point.
        """
        # Define the lat / lon
        longitude, latitude = current_point[0], current_point[1]

        # Calculate the angle between each neighbor
        angle_increment = 360 / number_of_neighbors

        # Calculate the neighbors coordinates
        neighbors = []
        for i in range(number_of_neighbors):
            angle = math.radians(angle_increment * i)
            dx = distance * math.cos(angle)
            dy = distance * math.sin(angle)
            neighbor = (longitude + dx, latitude + dy)

            # Find closest node
            closest_node, _, _ = self.quadtree.find_closest_node(neighbor, initial_search_radius=0.005,
                                                                 search_radius_increment=0.005,
                                                                 max_search_radius=0.025)
            # Append landOrWater value
            if closest_node is not None and closest_node.landOrWater == 1:
                neighbors.append((*neighbor, 1))
            elif closest_node is None or closest_node.landOrWater == 0:
                neighbors.append((*neighbor, 0))

        return neighbors

    def get_neighbors_astar_square(self, current_point, distance=500):
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
        lower_left = (longitude - half_distance, latitude - half_distance)
        lower_right = (longitude + half_distance, latitude - half_distance)
        upper_right = (longitude + half_distance, latitude + half_distance)
        upper_left = (longitude - half_distance, latitude + half_distance)

        # Middle of each leg
        lower_middle = (longitude, latitude - half_distance)
        right_middle = (longitude + half_distance, latitude)
        upper_middle = (longitude, latitude + half_distance)
        left_middle = (longitude - half_distance, latitude)

        # Center of each quadrant
        upper_left_quadrant = ((lower_left[0] + upper_left[0]) / 2, (lower_left[1] + upper_left[1]) / 2)
        upper_right_quadrant = ((lower_right[0] + upper_right[0]) / 2, (lower_right[1] + upper_right[1]) / 2)
        lower_left_quadrant = ((lower_left[0] + lower_right[0]) / 2, (lower_left[1] + lower_right[1]) / 2)
        lower_right_quadrant = ((upper_right[0] + lower_right[0]) / 2, (upper_right[1] + lower_right[1]) / 2)

        # Find closest node for each point and append to neighbors
        for point in [lower_left, lower_right, upper_right, upper_left,
                      lower_middle, right_middle, upper_middle, left_middle,
                      upper_left_quadrant, upper_right_quadrant, lower_left_quadrant, lower_right_quadrant]:
            closest_node, _, _ = self.quadtree.find_closest_node(point, initial_search_radius=0.005,
                                                                 search_radius_increment=0.005,
                                                                 max_search_radius=0.025)
            # Append landOrWater value
            if closest_node is not None and closest_node.landOrWater == 1:
                neighbors.append((*point, 1))
            elif closest_node is None or closest_node.landOrWater == 0:
                neighbors.append((*point, 0))

        return neighbors

    def h_euclidean(self, current_point, goal_point, visited_count=None):
        """
        Calculate the Euclidean distance from current point to the goal_point
        :param: current_point: current_point that heuristic is being calculated for
        :parma: goal_point:  the end position
        :param visited_count: Dictionary storing the number of times each node has been visited
        :return Euclidean distance:
        """
        current_point_longitude, current_point_latitude = current_point[0], current_point[1]
        goal_point_longitude, goal_point_latitude = goal_point[0], goal_point[1]

        # Calculate the Euclidean distance
        euclidean_distance = math.sqrt(
            (current_point_latitude - goal_point_latitude) ** 2
            + (current_point_longitude - goal_point_longitude) ** 2)

        # Additional penalty for visited nodes
        if visited_count and visited_count.get(current_point, 0) > 1 :
            penalty = float('inf')  # Set penalty to infinity for heavily visited nodes
        else:
            penalty = 0

        return euclidean_distance + penalty

    def h_manhattan(self, current_point, goal_point):
        """
        Calculate the Manhattan distance from current node to the goal_node
        :param: current_point: current_point that heuristic is being calculated for
        :parma: goal_point:  the end position
        :return Manhattan distance:
        """
        current_point_longitude, current_point_latitude = current_point[0], current_point[1]
        goal_point_longitude, goal_point_latitude = goal_point[0], goal_point[1]

        # Calculate the Manhattan distance
        return abs(current_point_latitude - goal_point_latitude) + abs(current_point_longitude - goal_point_longitude)

    #vvvvv PLOTTING METHODS
    def visualize_astar_path(self, start_point, goal_point, path, ax=None):
        """

        :param start_point:
        :param goal_point:
        :param start_closest_node:
        :param goal_closest_node:
        :return:
        """
        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(14, 9))

        self.quadtree.visualize_chart_data(ax)

        # Plot points (green / red)
        ax.scatter(start_point[0], start_point[1], c='green', marker='*', s=150, label='Start Point')
        ax.scatter(goal_point[0], goal_point[1], c='red', marker='*', s=150, label='Goal Point')

        # Plot the path
        if path:
            path_lon, path_lat = zip(*path)  # Unzip path coordinates
            ax.plot(path_lon, path_lat, color='blue', marker='o', markersize=3, linewidth=1, label='A* Path')

        # Setting Title
        ax.set_title('AStar Optimized Path', fontsize=20)
        ax.legend(loc='center right')

        plt.show()

    def visualize_astar_algorithm(self, start_point, goal_point, current_point, past_point_for_display):
        """

        :param start_point:
        :param goal_point:
        :param past_point_for_display:
        :return: figure
        """
        self.ax.clear()
        self.quadtree.visualize_chart_data(self.ax)

        # Plot past nodes as smaller grey dots
        for point in past_point_for_display:
            self.ax.scatter(point[0], point[1], facecolor='none', edgecolor='purple',
                            marker='o', linewidth=0.3, s=30, label='Past Node')
            # Plot dashed gray line from current point to goal point
            self.ax.plot([current_point[0], goal_point[0]], [current_point[1], goal_point[1]],
                         linewidth=0.3, linestyle='--', color='gray')

        self.ax.scatter(start_point[0], start_point[1], c='green', marker='*', s=150, label='Start Node')
        self.ax.scatter(goal_point[0], goal_point[1], c='red', marker='*', s=150, label='Start Node')
        self.ax.scatter(current_point[0], current_point[1], facecolor='none', edgecolor='blue',
                   marker='o', linewidth=1.0, s=100, label='Current Node')



        self.ax.set_title('AStar Algorithm In Motion', fontsize=20)
        plt.draw()
        plt.pause(0.01)



#### vvvv FUNCTIONS vvvv ####
def deserialize_quad_tree(file_path):
    """
    Method to load a .qtdata file containing Chart Data in a quad tree data structure format
    Parameter: file_path: including data file
    Return: quadtree
    """
    with open(file_path, 'rb') as f:
        quadtree = pickle.load(f)
    return quadtree


if __name__ == '__main__':
    # Load QuadTree Data
    quadtree_data_path = (
        '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
        'data/quad_tree/vineyardsound_coarse.qtdata'
    )
    quadtree_data = deserialize_quad_tree(quadtree_data_path)
    # Visualize Quad Tree Data
    # quadtree_data.visualize_quadtree()

    # node_data = quadtree_data.collect_node_data()
    # print(node_data)

    # Define Start and Goal Points
    """
    Define these initially as hard code start and goal points.  Once working
        clicks from the GUI Map will set the points from event handlers.
    """

    # Test Set 1 distance=0.009, number_of_neighbors=36
    # startPoint = (-70.87, 41.30)
    # goalPoint = (-70.85, 41.40)

    # Test Set 2 distance=1000, number_of_neighbors=4) square
    # startPoint = (-70.80, 41.30)
    # goalPoint = (-70.80, 41.40)

    # Test Set 3 distance=0.009, number_of_neighbors=36 radial / distance=1000, number_of_neighbors=4) square
    # startPoint = (-70.60, 41.493)
    # goalPoint = (-70.8411, 41.4347)

    # Test Set 4   distance=0.009, number_of_neighbors=36 / distance=1000, number_of_neighbors=4)square
    # startPoint = (-70.70527, 41.47)
    # goalPoint = (-70.8372, 41.46)

    # Test Set 5 distance=1000, number_of_neighbors=4) square
    # startPoint = (-70.65, 41.29)
    # goalPoint = (-70.84, 41.42)

    # Test Set 6 distance=1000, number_of_neighbors=4) square or radial
    # startPoint = (-70.75, 41.51)
    # goalPoint = (-70.8411, 41.4347)

    # Test Set 7 distance=1000, number_of_neighbors=4) square
    startPoint = (-70.80, 41.30)
    goalPoint = (-70.87, 41.45)

    # Test Set 7 distance=1000, number_of_neighbors=4) square
    # startPoint = (-70.63, 41.335)
    # goalPoint = (-70.87, 41.45)

    # Start time
    start_time = time.time()
    # Load Quad Data into AStarPathPlanner Class
    uuvIngressPath = AStarPathPlanner(quadtree_data)

    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("AStar Class Instantiated in:", elapsed_time, "seconds\n")

    # Test the astar_path method
    # Start time
    start_time = time.time()
    path = uuvIngressPath.astar_path(startPoint, goalPoint, distance=1000, number_of_neighbors=36)
    # print(type(path))
    if path:
        print("Optimal A* Path:")
        for lon, lat in path:
            print("Longitude:", lon, ", Latitude:", lat)
    else:
        print("Failed to find a path.")
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nAStar Path Calculated in:", elapsed_time, "seconds\n")

    uuvIngressPath.visualize_astar_path(startPoint, goalPoint, path)

