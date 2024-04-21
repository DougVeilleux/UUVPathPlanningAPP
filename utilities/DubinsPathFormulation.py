# DubinsPathFormulation.py
################################################################################
#
# Dubins Path Formulation following the work of Shkel & Lumelsky
# Shkel, Andrei and Lumelsky, Validimir - "Classification of the Dubins set"
#
# Ref: https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning
# /DubinsPath/dubins_path_planner.py
#
# Utilizing the Python Robotics work of author Atsushi Sakai
###############################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Union, Tuple, Any
from scipy.spatial.transform import Rotation as Rot


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

    def __post_init__(self) -> None:
        assert -180 <= self.longitude <= 180, "Longitude must be between -180 and 180 degrees"
        assert -90 <= self.latitude <= 90, "Latitude must be between -90 and 90 degrees"
        assert 0 <= self._heading_degrees <= 360, "Heading must be between 0 and 360 degrees"

    def __str__(self):
        return "longitude: " + str(self.longitude) + \
            ", latitude: " + str(self.latitude) + \
            ", heading: " + str(self.heading)


class DubinsPath:
    def __init__(self, start: Waypoint, end: Waypoint, radius: float,
                 paths: List[str] = None, step_size: float = 0.1,
                 selected_types: Union[List[str], None] = None):
        self.start = start
        self.end = end
        self.radius = radius
        self.curvature = 1 / radius
        self.paths = paths if paths is not None else ["LSL", "RSR", "LSR", "RSL", "RLR", "LRL"]
        self.step_size = step_size
        self.selected_types = selected_types

    def generateDubinsPath(self) -> tuple[Waypoint, Any | None, list[float | Any]]:
        """
        Generate Dubins paths between the start and end waypoints.

        :param step_size: Step size for Dubins path calculation.
        :param selected_types: List of selected Dubins path types.
        :return: List of Dubins path waypoints, modes, and lengths.
        """
        planning_funcs = [getattr(self, path) for path in self.paths]

        # Calculate the local goal lon, lat, heading
        l_rot = self.rot_mat_2d(self.start.heading)
        le_lonlat = np.stack([self.end.longitude - self.start.longitude,
                              self.end.latitude - self.start.latitude]).T @ l_rot
        local_goal_lon = le_lonlat[0]
        local_goal_lat = le_lonlat[1]
        local_goal_heading = self.end.heading - self.start.heading

        waypoint_list, modes, lengths = self.dubinsPathPlanningFromOrigin(planning_funcs)

        return waypoint_list, modes, lengths

    def dubinsPathPlanningFromOrigin(self, planning_funcs):
        """

        :param planning_funcs:
        :return:
        """
        dx, dy = self.end.longitude, self.end.latitude
        end_heading = self.end.heading
        d = math.hypot(dx, dy) * self.curvature

        theta = self.mod2pi(math.atan2(dy, dx))
        alpha = self.mod2pi(-theta)
        beta = self.mod2pi(end_heading - theta)

        best_cost = float("inf")
        b_t, b_p, b_q, b_mode = None, None, None, None

        for planner in planning_funcs:
            t, p, q, mode = planner(alpha, beta, d)
            if t is None:
                continue

            cost = (abs(t) + abs(p) + abs(q))
            if best_cost > cost:  # Select the minimum length one
                b_t, b_p, b_q, b_mode, best_cost = t, p, q, mode, cost

        lengths = [b_t, b_p, b_q]
        waypoint_list = self.generateLocalCourse(lengths, b_mode)

        lengths = [length / self.curvature for length in lengths]

        return waypoint_list, b_mode, lengths

    def generateLocalCourse(self, lengths, modes, current_length: float = 0.0):
        waypoints = []
        p_lon, p_lat, p_heading = [self.start.longitude], [self.start.latitude], [self.start.heading]
        for (mode, length) in zip(modes, lengths):
            if length == 0.0:
                continue
            # set origin state
            origin_lon, origin_lat, origin_heading = p_lon[-1], p_lat[-1], p_heading[-1]

            current_length += self.step_size
            while abs(current_length + self.step_size) <= abs(length):
                p_lon, p_lat, p_heading = self.interpolate(current_length, mode,
                                                           origin_lon, origin_lat, origin_heading,
                                                           p_lon, p_lat, p_heading)
                current_length += self.step_size
            p_lon, p_lat, p_heading = self.interpolate(length, mode,
                                                       origin_lon, origin_lat, origin_heading,
                                                       p_lon, p_lat, p_heading)
        waypoints.append((p_lon, p_lat, p_heading))
        return waypoints

    def interpolate(self, length, mode, origin_lon, origin_lat, origin_heading,
                    path_lon, path_lat, path_heading):
        if mode == "S":
            path_lon.append(origin_lon + length / self.curvature * math.cos(origin_heading))
            path_lat.append(origin_lat + length / self.curvature * math.sin(origin_heading))
            path_heading.append(origin_heading)
        else:  # curve L or R
            ldx = math.sin(length) / self.curvature
            ldy = 0.0
            if mode == "L":  # left turn
                ldy = (1.0 - math.cos(length)) / self.curvature
            elif mode == "R":  # right turn
                ldy = (1.0 - math.cos(length)) / -self.curvature
            gdx = math.cos(-origin_heading) * ldx + math.sin(-origin_heading) * ldy
            gdy = -math.sin(-origin_heading) * ldx + math.cos(-origin_heading) * ldy
            path_lon.append(origin_lon + gdx)
            path_lat.append(origin_lat + gdy)

            if mode == "L":  # left turn
                path_heading.append(origin_heading + length)
            elif mode == "R":  # right turn
                path_heading.append(origin_heading - length)

        return path_lon, path_lat, path_heading

    def LSL(self, alpha, beta, d):
        """
        LeftStraightLeft (LSL) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        sin_a, sin_b, cos_a, cos_b, cos_ab = self.calc_trig_funcs(alpha, beta)
        mode = ["L", "S", "L"]
        p_squared = 2 + d ** 2 - (2 * cos_ab) + (2 * d * (sin_a - sin_b))
        if p_squared < 0:  # invalid configuration
            return None, None, None, mode
        tmp = math.atan2((cos_b - cos_a), d + sin_a - sin_b)
        t = self.mod2pi(-alpha + tmp)
        p = math.sqrt(p_squared)
        q = self.mod2pi(beta - tmp)
        return t, p, q, mode

    def RSR(self, alpha, beta, d):
        """
        RightStraightRight (RSR) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        sin_a, sin_b, cos_a, cos_b, cos_ab = self.calc_trig_funcs(alpha, beta)
        mode = ["R", "S", "R"]
        p_squared = 2 + d ** 2 - (2 * cos_ab) + (2 * d * (sin_b - sin_a))
        if p_squared < 0:
            return None, None, None, mode
        tmp = math.atan2((cos_a - cos_b), d - sin_a + sin_b)
        t = self.mod2pi(alpha - tmp)
        p = math.sqrt(p_squared)
        q = self.mod2pi(-beta + tmp)
        return t, p, q, mode

    def RSL(self, alpha, beta, d):
        """
        RightStraightLeft (RSL) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        sin_a, sin_b, cos_a, cos_b, cos_ab = self.calc_trig_funcs(alpha, beta)
        mode = ["R", "S", "L"]
        p_squared = d ** 2 - 2 + (2 * cos_ab) - (2 * d * (sin_a + sin_b))
        if p_squared < 0:
            return None, None, None, mode
        p = math.sqrt(p_squared)
        tmp = math.atan2((cos_a + cos_b), (d - sin_a - sin_b)) - math.atan2(2.0, p)
        t = self.mod2pi(alpha - tmp)
        q = self.mod2pi(beta - tmp)
        return t, p, q, mode

    def LSR(self, alpha, beta, d):
        """
        LeftStraightRight (LSR) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        sin_a, sin_b, cos_a, cos_b, cos_ab = self.calc_trig_funcs(alpha, beta)
        mode = ["L", "S", "R"]
        p_squared = -2 + d ** 2 + (2 * cos_ab) + (2 * d * (sin_a + sin_b))
        if p_squared < 0:
            return None, None, None, mode
        p = math.sqrt(p_squared)
        tmp = math.atan2((-cos_a - cos_b), (d + sin_a + sin_b)) - math.atan2(-2.0, p)
        t = self.mod2pi(-alpha - tmp)
        q = self.mod2pi(-self.mod2pi(beta) + tmp)
        return t, p, q, mode

    def RLR(self, alpha, beta, d):
        """
        RightLeftRight (RLR) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        sin_a, sin_b, cos_a, cos_b, cos_ab = self.calc_trig_funcs(alpha, beta)
        mode = ["R", "L", "R"]
        tmp = (6.0 - d ** 2 + 2.0 * cos_ab + 2.0 * d * (sin_a - sin_b)) / 8.0
        if abs(tmp) > 1.0:
            return None, None, None, mode
        p = self.mod2pi(2 * math.pi - math.acos(tmp))
        t = self.mod2pi(alpha - math.atan2(cos_a - cos_b, d - sin_a + sin_b) + p / 2.0)
        q = self.mod2pi(alpha - beta - t + p)
        return t, p, q, mode

    def LRL(self, alpha, beta, d):
        """
        LeftRightLeft (LRL) Calculations
        :param alpha: heading (radians) at the initial Waypoint
        :param beta: heading (radians) at the final Waypoint
        :param d: Euclidean distance between Waypoint(i) and Waypoint(f)
        :return: t, p, q: constituent lengths of the segments
        """
        sin_a, sin_b, cos_a, cos_b, cos_ab = self.calc_trig_funcs(alpha, beta)
        mode = ["L", "R", "L"]
        tmp = (6.0 - d ** 2 + 2.0 * cos_ab + 2.0 * d * (- sin_a + sin_b)) / 8.0
        if abs(tmp) > 1.0:
            return None, None, None, mode
        p = self.mod2pi(2 * math.pi - math.acos(tmp))
        t = self.mod2pi(-alpha - math.atan2(cos_a - cos_b, d + sin_a - sin_b) + p / 2.0)
        q = self.mod2pi(self.mod2pi(beta) - alpha - t + self.mod2pi(p))
        return t, p, q, mode



    ### Helpers ###
    def mod2pi(self, theta):
        return self.angle_mod(theta, zero_2_2pi=True)

    def angle_mod(self, x, zero_2_2pi=False, degree=False):
        """
        Angle modulo operation
        Default angle modulo range is [-pi, pi)
        Parameters
        ----------
        x : float or array_like
            A angle or an array of angles. This array is flattened for
            the calculation. When an angle is provided, a float angle is returned.
        zero_2_2pi : bool, optional
            Change angle modulo range to [0, 2pi)
            Default is False.
        degree : bool, optional
            If True, then the given angles are assumed to be in degrees.
            Default is False.

        Returns
        -------
        ret : float or ndarray
            an angle or an array of modulated angle.

        Examples
        --------
        angle_mod(-4.0)
        2.28318531

        angle_mod([-4.0])
        np.array(2.28318531)

        angle_mod([-150.0, 190.0, 350], degree=True)
        array([-150., -170.,  -10.])

        angle_mod(-60.0, zero_2_2pi=True, degree=True)
        array([300.])

        """
        if isinstance(x, float):
            is_float = True
        else:
            is_float = False

        x = np.asarray(x).flatten()
        if degree:
            x = np.deg2rad(x)

        if zero_2_2pi:
            mod_angle = x % (2 * np.pi)
        else:
            mod_angle = (x + np.pi) % (2 * np.pi) - np.pi

        if degree:
            mod_angle = np.rad2deg(mod_angle)

        if is_float:
            return mod_angle.item()
        else:
            return mod_angle

    def rot_mat_2d(self, angle):
        """
        Create 2D rotation matrix from an angle
        Parameters
        ----------
        angle :
        Returns
        -------
        A 2D rotation matrix
        Examples
        --------
        angle_mod(-4.0)
        """
        return Rot.from_euler('z', angle).as_matrix()[0:2, 0:2]

    def calc_trig_funcs(self, alpha, beta):
        sin_a = math.sin(alpha)
        sin_b = math.sin(beta)
        cos_a = math.cos(alpha)
        cos_b = math.cos(beta)
        cos_ab = math.cos(alpha - beta)
        return sin_a, sin_b, cos_a, cos_b, cos_ab


if __name__ == '__main__':
    # Define start and end waypoints
    start_point = Waypoint(-70.85, 41.20, 90)  # Heading entered in degrees
    end_point = Waypoint(-70.75, 41.30, 45)  # Heading entered in degrees

    # Define radius (you may adjust this according to your specific application)
    radius = 2.0
    step_size = 0.09

    dubins_path = DubinsPath(start_point, end_point, radius, step_size=step_size)

    waypoint_list, modes, lengths = dubins_path.generateDubinsPath()

    # Extract lon, lat, and heading from waypoints
    lon_list, lat_list, heading_list = zip(*waypoint_list)

    # Plot the waypoints
    plt.figure(figsize=(10, 8))
    plt.scatter(lon_list, lat_list, color='blue', label='Waypoints')  # Plot waypoints as blue dots

    print("Before plotting loop")
    # Connect consecutive waypoints with lines
    for i in range(len(lon_list) - 1):
        print("Plotting line from ({}, {}) to ({}, {})".format(lon_list[i], lat_list[i], lon_list[i + 1],
                                                               lat_list[i + 1]))
        plt.plot([lon_list[i], lon_list[i + 1]], [lat_list[i], lat_list[i + 1]], 'k-',
                 linewidth=2)  # Connect consecutive points

    print("After plotting loop")
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Dubins Path')
    plt.grid(True)
    plt.legend()
    plt.show()

