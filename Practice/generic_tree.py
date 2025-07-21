class Node:
    def __init__(self, data = None, children = None):
        self.data = data
        self.children = children if children is not None else []

def print_tree(root):
    if root is None:
        return
    print(root.data) # Print the current node's data
    for child in root.children:
        print_tree(child)


def print_tree_detailed(root):
    if root is None:
        return

    print(f"{root.data} -> ", end = "") # Print the current node's data

    for child in root.children:
        print(child.data, end = " ") # Print each child's data

    print()
    
    for child in root.children:
        print_tree_detailed(child) # Recursive call to print each child's subtree


def take_input_level_wise():
    from collections import deque

    root_data = int(input("Enter the data for the root node: "))
    root = Node(root_data)
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        num_children = int(input(f"Enter the number of children for node {current_node.data}: "))
        
        for _ in range(num_children):
            child_data = int(input("Enter the data for the child node: "))
            child_node = Node(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    
    return root