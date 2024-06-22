import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  # Saving a node color in a graph
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Collect node colors to display

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def visualize_heap(root, key, i):

    if root is None:
        return Node(key)
    
    else:
        if i % 2:
            root.left = visualize_heap(root.left, key, i)
        else:
            root.right = visualize_heap(root.right, key, i)
    return root

preorder = []
def preorder_traversal(root,node_color):
  global inorder
  if root:
    print(root.val)
    root.color = node_color[len(preorder)]
    preorder.append(root.val)
    preorder_traversal(root.left, node_color)
    preorder_traversal(root.right, node_color)

inorder = []
def inorder_traversal(root,node_color):
    global inorder
    if root:
        inorder_traversal(root.left , node_color)
        
        print(root.val)
        root.color = node_color[len(inorder)]
        inorder.append(root.val)
        
        inorder_traversal(root.right, node_color)

nums = [4, 10, 3, 5, 1, 2 ,3]
heapq.heapify(nums)


# Creating the tree
root = Node(nums[0])
root.left = Node(nums[1])
root.right = Node(nums[2])
root.left.left = Node(nums[3])
root.left.right = Node(nums[4])
root.right.left = Node(nums[5])

# Displaying the tree
# draw_tree(root)

color_gen =[]
for i in range (0, len(nums)-1):
    color_gen.append([int(255/len(nums)*i),int(255/len(nums)*i),int(255/len(nums)*i)])

node_color=[ '#%02x%02x%02x' % (c[0],c[1],c[2]) for c in color_gen ]

#in order traversal

inorder_traversal(root, node_color)

# Displaying the tree
draw_tree(root)

#Preorder traversal

preorder_traversal(root, node_color)

# Displaying the tree
draw_tree(root)