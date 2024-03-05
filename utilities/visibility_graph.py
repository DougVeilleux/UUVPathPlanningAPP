# visibility_graph.py


import math
import heapq
import pickle

from utilities.quad_tree_geodata_multipolygon import *


class VisibilityGraph:
    """
    Class utilized to read a quad tree data structure and refactor for
        direct us in the an A* path planning algorithm
    Parameter: quadtree, quadtree data set
    Attributes:
        nodes, nodes of the quadtree
        graph, visbility graph
    """
    def __init__(self, quadtree):
        self.quadtree = quadtree
        self.nodes = self.extract_nodes()
        self.graph = self.build_visibility_graph()
