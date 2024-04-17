#DubinsPathFormulation.py
################################################################################
#
# Dubins Path Formulation following the work of Shkel & Lumelsky
# Shkel, Andrei and Lumelsky, Validimir - "Classification of the Dubins set"
#
###############################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Waypoint:
    """
    Dubins requires a Point containing (x,y) coordinate and a heading angle (theta)
    A Point shall be entered as (longitude, latitude, heading)
    :param: longitude in decimal degrees
    :param: latitude in decimal degrees
    :param: heading in decimal degrees
    """
    longitude: float
    latitude: float
    _heading_degrees: float

    @property
    def heading(self):
        return math.radians(self._heading_degrees)

    @heading.setter
    def heading(self, value):
        # Convert radians to degrees when setting the heading
        self._heading_degrees = math.degrees(value)

    def __str__(self):
        return "longitude: " + str(self.longitude) + \
            ", latitude: " + str(self.latitude) +\
            ", heading: " + str(self.heading)

@dataclass
class DubinsPath:
    start: Waypoint
    end: Waypoint
    radius: float
    paths: list = None

    def __post_init__(self):
        if self.paths is None:
            self.paths = []
            self.generatePaths()

    def generatePaths(self):
        alpha = self.start.heading
        beta = self.end.heading
        d = math.sqrt((self.end.longitude - self.start.longitude)**2 +
                      (self.end.latitude - self.start.latitude)**2)
        self.paths.append(self.LSL(alpha, beta, d))
        self.paths.append(self.RSR(alpha, beta, d))
        self.paths.append(self.RSL(alpha, beta, d))
        self.paths.append(self.LSR(alpha, beta, d))
        self.paths.append(self.RLR(alpha, beta, d))
        self.paths.append(self.LRL(alpha, beta, d))

    def LSL(self, alpha, beta, d):
        """
        LeftStraightLeft (LSL) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        temp0 = d + math.sin(alpha) - math.sin(beta)
        temp1 = math.atan2((math.cos(beta) - math.cos(alpha)), temp0)
        pSquared = 2 + d**2 - (2*math.cos(alpha-beta)) + (2*d*(math.sin(alpha) - math.sin(beta)))
        if pSquared < 0:
            print('No LSL Path')
            t, p, q = -1, -1, -1
        else:
            t = (-alpha + temp1) % (2*math.pi)
            p = math.sqrt(pSquared)
            q = (beta - temp1) % (2*math.pi)

        return t, p, q

    def RSR(self, alpha, beta, d):
        """
        RightStraightRight (RSR) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        temp0 = d - math.sin(alpha) + math.sin(beta)
        temp1 = math.atan2((math.cos(alpha) - math.cos(beta)), temp0)
        pSquared = 2 + d**2 - (2*math.cos(alpha - beta)) + 2*d*(math.sin(beta) - math.sin(alpha))
        if pSquared < 0:
            print('No RSR Path')
            t, p, q = -1, -1, -1
        else:
            t = (alpha - temp1) % (2*math.pi)
            p = math.sqrt(pSquared)
            q = (-beta + temp1) % (2*math.pi)

        return t, p, q

    def RSL(self, alpha, beta, d):
        """
        RightStraightLeft (RSL) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        temp0 = d + math.sin(alpha) + math.sin(beta)
        temp1 = math.atan2((-math.cos(alpha) - math.cos(beta)), temp0)
        pSquared = -2 + d**2 - (2 * math.cos(alpha - beta)) + 2 * d * (math.sin(beta) - math.sin(alpha))
        if pSquared < 0:
            print('No RSL Path')
            t, p, q = -1, -1, -1
        else:
            p = math.sqrt(pSquared)
            temp2 = math.atan2(-2, p)
            t = (-alpha + temp1 - temp2) % (2*math.pi)
            q = (-beta -temp2) % (2*math.pi) + temp1

        return t, p, q

    def LSR(self, alpha, beta, d):
        """
        LeftStraightRight (LSR) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        temp0 = d - math.sin(alpha) - math.sin(beta)
        temp1 = math.atan2((math.cos(alpha) + math.cos(beta)), temp0)
        pSquared = -2 + d**2 + (2 * math.cos(alpha - beta)) + 2*d*(math.sin(alpha) + math.sin(beta))
        if pSquared < 0:
            print('No LSR Path')
            t, p, q = -1, -1, -1
        else:
            p = math.sqrt(pSquared)
            temp2 = math.atan2(2, p)
            t = (alpha - temp1 + temp2) % (2*math.pi)
            q = (beta + temp2) % (2*math.pi) + temp1

        return t, p, q

    def RLR(self, alpha, beta, d):
        """
        RightLeftRight (RLR) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        temp0 = d - math.sin(alpha) + math.sin(beta)
        temp1 = math.atan2((math.cos(alpha) - math.cos(beta)), temp0)
        p = (math.acos((6 - d**2 + 2 * math.cos(alpha - beta) +
                    2 * d * (math.sin(alpha) - math.sin(beta))) / 8)) % 2 * math.pi
        if abs(p) > 1:
            print('No LRL Path')
            t, p, q = -1, -1, -1
        else:
            p = p
            t = (alpha - temp1) + (p/2) % (2*math.pi)
            q = (alpha - beta + t) + p % (2*math.pi)

        return t, p, q

    def LRL(self, alpha, beta, d):
        """
        LeftRightLeft (LRL) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        temp0 = d + math.sin(alpha) - math.sin(beta)
        temp1 = math.atan2((-math.cos(alpha) + math.cos(alpha)), temp0)
        p = (math.acos((6 - d**2 + 2*math.cos(alpha - beta) +
                       2*d*(math.sin(alpha) - math.sin(beta)))/8)) % 2*math.pi
        if abs(p) > 1:
            print('No LRL Path')
            t, p, q = -1, -1, -1
        else:
            p = p
            t = (-alpha - temp1 + p/2) % (2*math.pi)
            q = (beta + 2*p) % (2*math.pi) - alpha

        return t, p, q


if __name__ == '__main__':
    # Define start and end waypoints
    start_point = Waypoint(-70.85, 41.20, 90)  # Heading entered in degrees
    end_point = Waypoint(-70.75, 41.30, 45)  # Heading entered in degrees

    # Define radius (you may adjust this according to your specific application)
    radius = 20.0

    # Create DubinsPath object
    dubins_path = DubinsPath(start_point, end_point, radius)

    # Generate paths
    dubins_path.generatePaths()

    # Plot the start and end points
    plt.plot(start_point.longitude, start_point.latitude, 'ro', label='Start')
    plt.plot(end_point.longitude, end_point.latitude, 'go', label='End')

    # Plot the Dubins paths
    for i, path in enumerate(dubins_path.paths):
        # Extracting path segments
        t, p, q = path

        # Plotting the path segment
        plt.plot([start_point.longitude, start_point.longitude + p * np.cos(t)],
                 [start_point.latitude, start_point.latitude + p * np.sin(t)], label=f'Path {i + 1}')
        plt.plot([end_point.longitude, end_point.longitude + p * np.cos(q)],
                 [end_point.latitude, end_point.latitude + p * np.sin(q)])

    # Add labels and legend
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Dubins Paths')
    plt.legend()
    plt.grid()

    # Show plot
    plt.show()
