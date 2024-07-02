# Save this as `leaf_tree.py`

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __iter__(self):
        return iter(self.children)

# Build Leaf Tree
def build_leaf_tree():
    leaf_nodes = [
        Node([5, 6]),   # Leaf Node
        Node([7, 4, 5]),  # Leaf Node
        Node([3]),      # Leaf Node
        Node([6]),      # Leaf Node
        Node([6, 9]),   # Leaf Node
        Node([7]),      # Leaf Node
        Node([5]),      # Leaf Node
        Node([9, 8]),   # Leaf Node
        Node([6])       # Leaf Node
    ]
    return leaf_nodes

# Build the tree structure
def build_tree_structure(level, node, maxi):
    if level == -1:
        return node.value[0]  # assuming the value is a list with one element

    if maxi:
        evaluate_max = -100000
        for i in node:
            evaluation = build_tree_structure(level - 1, i, False)
            evaluate_max = max(evaluate_max, evaluation)
        node.value.append(evaluate_max)  # Store maximum value on parent node
        return evaluate_max
    else:
        evaluate_min = 100000
        for i in node:
            evaluation = build_tree_structure(level - 1, i, True)
            evaluate_min = min(evaluate_min, evaluation)
        node.value.append(evaluate_min)  # Store minimum value on parent node
        return evaluate_min

# Draw a Tree
def draw_tree(node, level=0):
    if node is None:
        return
    print('  ' * level, node.value)
    for child in node.children:
        draw_tree(child, level + 1)

def build_tree(leaf_nodes):
    # build the tree structure
    node3 = Node([])
    node3.add_child(leaf_nodes[0])
    node3.add_child(leaf_nodes[1])

    node4 = Node([])
    node4.add_child(leaf_nodes[2])
    node4.add_child(leaf_nodes[3])

    node5 = Node([])
    node5.add_child(leaf_nodes[4])
    node5.add_child(leaf_nodes[5])

    node6 = Node([])
    node6.add_child(leaf_nodes[6])
    node6.add_child(leaf_nodes[7])

    node2 = Node([])
    node2.add_child(node3)
    node2.add_child(node4)

    node1 = Node([])
    node1.add_child(node2)
    node1.add_child(node5)
    node1.add_child(node6)

    return node1

def main():
    leaf_nodes = build_leaf_tree()
    root_node = build_tree(leaf_nodes)
    result = build_tree_structure(2, root_node, True)
    draw_tree(root_node)

if __name__ == '__main__':
    main()
