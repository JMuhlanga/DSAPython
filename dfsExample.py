# Depth First Search Example

class TreeNode:
    def __init__(self,data, left = None, right = None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # In-order Traversal
    def in_order(self, current_node):
        current_node = root
        if current_node:
            self.in_order(current_node.left_child)
            print(current_node.data)
            self.in_order(current_node.right_child)
    # Pre-order Traversal
    def pre_order(self,current_node):
        if current_node:
            print(current_node.data)
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)

# DFS on a graph
def dfs(visited_vertices,graph,current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices,graph,adjacent_vertex)
