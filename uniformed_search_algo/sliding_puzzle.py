import copy


def print_puzzle(state):
    for row in state:
        print(row)
    print()


def get_neighbors(state):
    neighbors = []
    zero_pos = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
    x, y = zero_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def dfs(start, goal):
    stack = [start]
    visited = set()
    visited.add(tuple(map(tuple, start)))

    while stack:
        current_state = stack.pop()

        if current_state == goal:
            print("Goal state reached!")
            print_puzzle(current_state)
            return True

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                stack.append(neighbor)

    print("Goal state not found.")
    return False


# Define the start and goal states
start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Perform DFS to solve the puzzle
dfs(start_state, goal_state)
