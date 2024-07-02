import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()
G.add_nodes_from(range(1, 7))
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 6), (5, 6)])

# Define the heuristics for each node
heuristics = {1: '5', 2: '4', 3: '2', 4: '3', 5: '1', 6: '0'}


# Implement Best first search algorithm
def best_first_search(graph, start, goal, heuristics):
    visited = []
    queue = [(start, [start])]

    while queue:
        node, path = queue.pop(0)
        visited.append(node)

        if node == goal:
            return path

        neighbors = sorted(graph.neighbors(node), key=lambda x: heuristics[x])
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))


# find the best path
start_node = 1
goal_node = 6
best_path = best_first_search(G, start_node, goal_node, heuristics)

# Visualize the graph with the best path
pos = {1: (1, 3), 2: (2, 4), 3: (2, 2), 4: (3, 5), 5: (3, 1), 6: (4, 3)}
nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue')

# Draw heuristic values near nodes
nx.draw_networkx_labels(G, pos, labels={node: f"{node}\n{heuristics[node]})"
                                        for node in G.nodes()}, font_size=12, font_color='black',
                        verticalalignment='center')

nx.draw_networkx_nodes(G, pos, nodelist=best_path, node_color='red', node_size=1000)
nx.draw_networkx_edges(G, pos, edgelist=[(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)], edge_color='red', width=2)
plt.title("Best First Search")
plt.show()