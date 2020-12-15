# -*- coding: utf-8 -*-

from functions import min_prims_edge, initialize_prims, is_spanning, cost, E
from drawing import show_weighted_graph, draw_subtree

"""declaration and initiation of prims algorithm."""
def prims_algorithm(G, starting_vertex, show_graph = False, show_cost = False):
    """
Parameters
----------
G : classes.graph.Graph
    
starting_vertex : int
    initialiing the minimum spanning tree, vertex chosen at random
show_graph : boolean
    initializing value, which switches once spanning tree is contructed
show_cost : boolean

"""
    if show_graph == True:
        show_weighted_graph(G)
        
    T = initialize_prims(G, starting_vertex)
    
    while is_spanning(G, T) == False:
        e = min_prims_edge(G, T)
        T.add_edge(e[0], e[1])
        if show_graph == True:
            draw_subtree(G, T)
            
    if show_cost == True:
        c = sum([cost(G, e) for e in E(T)])
        print(f'The cost of this spanning tree is {c}')
    return T
