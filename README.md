
"""
UUV Path Planner App

Capstone project employing a path planning element utilizing the AStar algorithm to solve 
the optimized path between two points.  A quad tree data structure is utilized to build and 
store the land / water boundaries which are used as the "truth" table for the AStar algo when
solving for the optimal path.


Project Structure
    data
    -contains the NOAA ENC files, the processed Shapefiles, the serialized .qtdata from the quadtree code

    src
    -contains the uuvMissionPlanner App and subsequent display pages code 
        (start, path planning, and survey planning)

    test
    -contains varrious testing script to confirm functionality of code chunks used in the App

    utilities
    -contains all the core functionality of the project
        -ShapefileHandler.py - reads a shapefile and prepares it for use with the Quad Tree creation
            numerous mehtods and helpers contianed within the class
        -QuadTreeGeodata.py - generates and writes serialized quadtree data structure to .qtdata file 
            which is utilized by the AStar algorithm.
        -AstarPathPlanner.py - the AStar Path Optimization alogorithm and associated helper
            methods used for the project.
        -DubinsPathFormulation - the early stages of the UUV turning control which is utilized in the 
            Survey Complete Coverage Path Planning algorithms.  Still a work in process.

        -QuadTreePoints.py - initial testing script utilized to work thru the details of the Quad Tree
            functionality on a simplified and random point set.  Just included for completness of the
            overall semester effort.



"""
