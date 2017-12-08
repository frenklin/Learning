#!/usr/bin/env python

class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None
        self.rand = None


def clone(root):
    if not root:
        return None

    result = Node(root.x)
    nodes = {}

    def get_node_x(node):
        if node:
            return node.x

    def build_dict(curr):            
        nodes.update({curr.x: Node(curr.x)})
        if curr.left:            
            build_dict(curr.left)
        if curr.right:            
            build_dict(curr.right)    

    def build_tree(curr, new_curr):                        
        if curr.left:
            new_curr.left = nodes[curr.left.x]
            build_tree(curr.left, new_curr.left)

        if curr.right:
            new_curr.right = nodes[curr.right.x]
            build_tree(curr.right, new_curr.right)
        
        if curr.rand:
            new_curr.rand = nodes[curr.rand.x]

    build_dict(root)
    build_tree(root, result) 

    return result



root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.right.rand = root_node


def get_node_val(node):
    if node:
        return node.x
    return "None"

def print_nodes(node):
    print("{} rnd -> {} ".format(node.x, get_node_val(node.rand)))
    if node.left:
        print_nodes(node.left)    
    if node.right:
        print_nodes(node.right)
    
print("original")
print_nodes(root_node)
clone = clone(root_node) 

root_node.x = -100
print("original -100")
print_nodes(root_node)

print("clone of original")
print_nodes(clone)