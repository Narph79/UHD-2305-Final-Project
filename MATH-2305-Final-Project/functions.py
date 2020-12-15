import networkx as nx

def V(graph):
    """ takes data from the graph.txt file and creats a list of nodes """
    return list(graph.nodes())

def E(graph):
    """ Takes data from the graph.txt file and creats a list of edges """
    return list (graph.edges())

def initialize_prims(graph, v):
    if v not in V(graph):
        return ("Error  ")
    else:
        T = nx.Graph()
        T.add_node(v)
        return T
    
def is_spanning(graph, subgraph):
    return V(graph) == V(subgraph)

def cost(G, e):
    """ 
    Parameters
    ----------
    G : classes.graph.Graph
        Contains the list of 
    e : tuple
    
    Returns
    ----------
    Float
        The Weight of the edge
    """
    
    return G[e[0]] [e[1]] ['weight']

def possible_edges(G, T):
    """
    Parameters
    ----------
    G : classes.graph.Graph
    T : classes.graph.Graph
    Returns
    ----------
    list
        a list of tuples that represent the possible edges
    """
    return [e for e in list(G.edges(V(T))) 
            if e[0] not in V(T) or e[1] not in V(T)]

def min_prims_edge(G, T):
    """ Gets the graph and the vertex
    
    Parameters
    ----------
    G : classes.graph.Graph
    T : classes.graph.Graph
    
    Returns
    ----------
    Tuple
        the tuple of the list that has the lowest weight
    """
    # Call the possible_edges function
    f = possible_edges(G,T)
    # creats a temporary variable to hold the weighted of the first edge)
    temp = cost(G, f[0])
    # assign k as the first array in case the fist edge has the lowest weighted
    k = 0
    # finds the lowest weighted edge out of the possible edges
    for element in range(0, len(f)):
        if cost(G, f[element]) < temp:
            temp = cost(G,f[element])
            k = element
        
    return f[k]
    
    
