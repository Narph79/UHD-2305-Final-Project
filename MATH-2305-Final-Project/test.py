import networkx as nx
from functions import *
from algorithms import prims_algorithm
#Test.py holds all the functions that are tested before being incorporated into main, functions, etc.
graph_data = open('test-graph/G2.txt', 'r')

G = nx.read_weighted_edgelist(graph_data, nodetype= int)

T = initialize_prims(G,3)

print(f'The vertex of  T is V(T) = {V(T)}')
print('')
print(f'The edge of  T is E(T) = {E(T)}')

#T = prims_algorithm(G, 0)

f = possible_edges(G,T)
e = min_prims_edge(G, T)
temp = cost(G, f[0])
for element in range(0, len(f)):
    if cost(G, f[element]) < temp:
        temp = cost(G,f[element])
        k = element
else:
    k = 0
        
