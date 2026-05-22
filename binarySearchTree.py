# Binary Search Tree Example
from logging import root


class TreeNode:
    def __init__(self,data, left = None, right = None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #  Binary to search  for Node in Tree
    def search(self,search_value):
        current_node = root

        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False

    # Function to insert in a Binary Search Tree
    def insert(self,data):
        new_node = TreeNode(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left_child == None:
                        return
                    else:
                        current_node = current_node.left_child
                elif data > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child
    # Function to find minimum value node
    def find_min(self):
        # Set current_node as the root
        current_node = self.root

        # Check if the tree is empty
        if current_node is None:
            return None

        # Iterate over the nodes of the appropriate subtree (always left)
        while current_node.left_child:
            # Update current_node to the left child
            current_node = current_node.left_child

        return current_node.data