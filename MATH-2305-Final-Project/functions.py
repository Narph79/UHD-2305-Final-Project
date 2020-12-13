import networkx as nx

def V(graph):
    return list(graph.nodes())

def E(graph):
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
    return G[e[0]] [e[1]] ['weight']

def possible_edges(G, T):
    return [e for e in list(G.edges(V(T))) 
            if e[0] not in V(T) or e[1] not in V(T)]

def min_prims_edge(G, T):
    f = possible_edges(G,T)
    temp = cost(G, f[0])
    k = 0
    for element in range(0, len(f)):
        if cost(G, f[element]) < temp:
            temp = cost(G,f[element])
            k = element
        
    return f[k]
    
    