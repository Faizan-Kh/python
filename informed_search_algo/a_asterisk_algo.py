import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Define the graph
G = nx.Graph()
G.add_nodes_from(range(1, 7))
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 6), (5, 6)])

# Define the heuristics for each node
heuristics = {1: 5, 2: 4, 3: 2, 4: 3, 5: 1, 6: 0}

# Define the cost for each edge
edge_costs = {
    (1, 2): 1,
    (1, 3): 2,
    (2, 4): 2,
    (2, 5): 3,
    (3, 6): 1,
    (4, 6): 3,
    (5, 6): 1
}


# Implement A* search algorithm
def a_star_search(graph, start, goal, heuristics, edge_costs):
    open_set = []
    heapq.heappush(open_set, (0, start, [start]))
    g_costs = {node: float('inf') for node in graph.nodes}
    g_costs[start] = 0
    visited = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        visited.add(current)

        for neighbor in graph.neighbors(current):
            if neighbor in visited:
                continue

            tentative_g_cost = g_costs[current] + edge_costs.get((current, neighbor), float('inf'))

            if tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristics[neighbor]
                heapq.heappush(open_set, (f_cost, neighbor, path + [neighbor]))

    return None


# Find the best path using A* search
start_node = 1
goal_node = 6
best_path = a_star_search(G, start_node, goal_node, heuristics, edge_costs)

# Visualize the graph with the best path
pos = {1: (1, 3), 2: (2, 4), 3: (2, 2), 4: (3, 5), 5: (3, 1), 6: (4, 3)}
nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue')

# Draw heuristic values near nodes
nx.draw_networkx_labels(G, pos, labels={node: f"{node}\n{heuristics[node]}"
                                        for node in G.nodes()}, font_size=12, font_color='black',
                        verticalalignment='center')

nx.draw_networkx_nodes(G, pos, nodelist=best_path, node_color='red', node_size=1000)
nx.draw_networkx_edges(G, pos, edgelist=[(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)],
                       edge_color='red', width=2)
plt.title("A* Search")
plt.show()
