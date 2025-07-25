# Node class for a Binary Search Tree
class BSTNode:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.left = None  # Left child
        self.right = None  # Right child

from collections import deque

def build_tree_from_level_order(arr):
    if not arr or arr[0] is None:
        return None
    
    root = BSTNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            current.left = BSTNode(arr[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            current.right = BSTNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root

def print_bst(root):
    if root is None:
        return
    print_bst(root.left)
    print(root.data, end = ' ') # Inorder traversal 
    print_bst(root.right)

def print_binary_search_tree(root):
    if root is None:
        return
    
    print(root.data, end = ' -> ') # Print the current node's data
    
    if root.left is not None:
        print(f"L: {root.left.data},", end = ' ')
    else:
        print("L: None,", end = ' ')
    if root.right is not None:
        print(f"R: {root.right.data}", end = '\n')
    else:
        print("R: None")

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize an empty tree

    # Public method to insert data into the BST
    def insert(self, data):
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = BSTNode(data)
        else:
            # Otherwise, use the helper method to insert recursively
            self._insert(self.root, data)

    # Private helper method for recursive insertion
    def _insert(self, root, data):
        if root is None:
            return BSTNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    # Public method to search for data in the BST
    def search(self, data):
        return self._search(self.root, data)

    # Private helper method for recursive search
    def _search(self, root, data):
        if root is None:
            return False  # Data not found
        if root.data == data:
            return True  # Data found
        elif data < root.data:
            # Search in the left subtree
            return self._search(root.left, data)
        else:
            # Search in the right subtree
            return self._search(root.right, data)

    # Public method to delete a node from the BST
    def delete(self, data):
        self.root = self._delete(self.root, data)

    # Private helper method for recursive deletion
    def _delete(self, root, data):
        if root is None:
            return root  # Node not found, do nothing

        if data < root.data:
            # Recur on the left subtree
            root.left = self._delete(root.left, data)
        elif data > root.data:
            # Recur on the right subtree
            root.right = self._delete(root.right, data)
        else:
            # Node to be deleted is found

            # Case 1: Node has no left child
            if root.left is None:
                return root.right

            # Case 2: Node has no right child
            elif root.right is None:
                return root.left
            
            # Case 3: Node has two children
            # Find the inorder successor (smallest node in the right subtree)
            min_larger_node = root.right
            while min_larger_node.left is not None:
                min_larger_node = min_larger_node.left
            
            # Copy the inorder successor's value to the current node
            root.data = min_larger_node.data
            
            # Delete the inorder successor
            root.right = self._delete(root.right, min_larger_node.data)

        return root  # Return the (possibly updated) node
