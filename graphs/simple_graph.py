# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 02:09:55 2024

@author: Faizan
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = range(1, 11)
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6), (5, 7), (6, 7), (6, 8), (8, 9), (8, 10)]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# visualizing the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_weight='bold')
plt.title("Graph with 10 nodes and multiple connections")
plt.show()
