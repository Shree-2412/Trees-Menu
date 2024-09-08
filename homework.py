class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Preorder traversal (Root -> Left -> Right)
def preorder_traversal(node):
    if node:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Inorder traversal (Left -> Root -> Right)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# Postorder traversal (Left -> Right -> Root)
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

# Function to manually create a sample tree
def create_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

# Function to handle menu choices
def menu():
    root = None
    while True:
        print("\nMenu:")
        print("1. Create a sample tree")
        print("2. Preorder Traversal")
        print("3. Inorder Traversal")
        print("4. Postorder Traversal")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            root = create_sample_tree()
            print("Sample tree created.")
        elif choice == '2':
            if root:
                print("Preorder Traversal:")
                preorder_traversal(root)
                print()
            else:
                print("Please create a tree first.")
        elif choice == '3':
            if root:
                print("Inorder Traversal:")
                inorder_traversal(root)
                print()
            else:
                print("Please create a tree first.")
        elif choice == '4':
            if root:
                print("Postorder Traversal:")
                postorder_traversal(root)
                print()
            else:
                print("Please create a tree first.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
