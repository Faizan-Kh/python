graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['H', 'I'],
    'G': [],
    'H': [],
    'I': []
}


def bfs(graph, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        if s == goal:
            print("\nGoal state reached:", goal)
            return

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print("\nGoal state not found in the graph")


bfs(graph, 'A', 'G')
