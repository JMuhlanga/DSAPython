# Trees and Graphs Examples

# Binary Tree implementation
## Tree Node class
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left_child = left
        self.right_child = right

# Building a simple tree
node1 = TreeNode('B')
node2 = TreeNode('C')
root_node = TreeNode('A', node1, node2)

# Graph Implementation
## Graph class
class Graph:
    def __init__(self):
        self.vertices = {}

    # Add Vertex method
    def add_vertex(self,vertex):
        self.vertices[vertex] = []

    # Add Edge method
    def add_edge(self, source, target):
        self.vertices[source].append(target)

## We can build a graph with

### Graph class instatiation
my_graph = Graph()

### Adding Vertices
my_graph.add_vertex('David')
my_graph.add_vertex('Miriam')
my_graph.add_vertex('Martin')

### Adding Edges
my_graph.add_edge('David', 'Miriam')
my_graph.add_edge('David', 'Martin')
my_graph.add_edge('Miriam', 'Martin')

# We can print the vertices
print(my_graph.vertices)