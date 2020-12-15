# -*- coding: utf-8 -*-


import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *

graph_data = open('test-graph/G2.txt', 'r')

G = nx.read_weighted_edgelist(graph_data, nodetype= int)
"""
Parameters 
---------
graph_data  : boolean

nodetype : int

"""

T= prims_algorithm(G, 3, show_graph = True, show_cost = True)
"""
Parameters
----------
G : int

show_graph : boolean

show_cost : boolean

"""
