class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
    
    print_binary_search_tree(root.left) # Recursive call for left child
    print_binary_search_tree(root.right) # Recursive call for right child

# Function to return complex binary trees
def predefined_bst_inputs():
    # Tree 1: Basic Tree with height 3
    root1 = BSTNode(10)
    root1.left = BSTNode(5)
    root1.right = BSTNode(15)

    # Tree 2: Slightly complex tree with height 4
    root2 = BSTNode(20)
    root2.left = BSTNode(10)
    root2.right = BSTNode(30)
    root2.left.left = BSTNode(5)
    root2.left.right = BSTNode(15)
    root2.right.left = BSTNode(25)
    root2.right.right = BSTNode(35)

    # Tree 3: More complex tree with height 5
    root3 = BSTNode(40)
    root3.left = BSTNode(20)
    root3.right = BSTNode(60)
    
    root3.left.left = BSTNode(10)
    root3.left.right = BSTNode(30)

    root3.left.left.left = BSTNode(5)
    root3.left.left.right = BSTNode(15)
    
    root3.left.right.left = BSTNode(25)
    root3.left.right.right = BSTNode(35)

    root3.right.left = BSTNode(50)
    root3.right.right = BSTNode(70)
    
    root3.right.left.right = BSTNode(55)

    root3.right.right.left = BSTNode(65)
    root3.right.right.right = BSTNode(75)

    return root1, root2, root3

# Getting predefined binary search trees
root1, root2, root3 = predefined_bst_inputs()

# Properties and Visualization
# root1: Contains 6 nodes, Height = 3
# Structure:
#        10
#       /  \
#      5   15
# root2: Contains 7 nodes, Height = 4
# Structure:
#        20
#       /  \
#      10   30
#     / \   / \
#    5  15 25 35
# root3: Contains 15 nodes, Height = 5
# Structure:
#        40
#       /  \
#      20   60
#     / \   / \
#    10 30 50 70
#   / \  / \  / \
#  5 15 25 35 55 65
