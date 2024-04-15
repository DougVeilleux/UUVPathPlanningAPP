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
        # convert radians to degrees when setting the heading
        self._heading_deg = math.degrees(value)

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
        self.paths.append(self.LSL())
        self.paths.append(self.RSR())
        self.paths.append(self.RSL())
        self.paths.append(self.LSR())
        self.paths.append(self.RLR())
        self.paths.append(self.LRL())

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
            t = (-alpha + temp1) % 2*math.pi
            p = math.sqrt(pSquared)
            q = (beta - temp1) % 2*math.pi

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
        pSquared = 2 + d * d - (2 * math.cos(alpha - beta)) + 2 * d * (math.sin(beta) - math.sin(alpha))
        if pSquared < 0:
            print('No RSR Path')
            t, p, q = -1, -1, -1
        else:
            t = (alpha - temp1) % 2 * math.pi
            p = math.sqrt(pSquared)
            q = (-beta + temp1) % 2 * math.pi

        return t, p, q



    def RSL(self, alpha, beta, d):
        pass
    def LSR(self, alpha, beta, d):
        pass
    def RLR(self, alpha, beta, d):
        pass
    def LRL(self, alpha, beta, d):
        pass


if __name__ == '__main__':

    # Example usage
    waypoint = Waypoint(-70.85, 41.20, 90)  # Heading entered in degrees
    print(waypoint)  # Output: longitude: 0, latitude: 0, heading: 1.5707963267948966 radians
    print("Heading in degrees:", waypoint._heading_degrees)  # Output: 90.0