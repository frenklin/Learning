#!/usr/bin/env python
"""DFS BFS"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys
from collections import deque

class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = list()  #linkedlist
    
    def addAdjacentNode(self, id_node):
        self.adjacent.append(id_node)

class Graph:
    def __init__(self):
        self.nodes = dict()

    def addEdge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = Node(src)
        
        if not dst in self.nodes:
            self.nodes[dst] = Node(dst)

        self.nodes[src].addAdjacentNode(dst)
        self.nodes[dst].addAdjacentNode(src)
    
    def getNode(self, id):
        return self.nodes[id]

class GraphSearch:

    def __init__(self, graph):
        self.graph = graph    
    

    def dfs(self, src, dst):
        if not src in self.graph.nodes or not dst in self.graph.nodes :
            return False
        visited = list()
        return self.hasPathDFS(src, dst, visited)

    
    def hasPathDFS(self, src, dst, visited):        
        if src in visited:
            return False
        visited.append(src)
        if src == dst:            
            return True        
        for child in self.graph.getNode(src).adjacent:            
            if(self.hasPathDFS(child, dst, visited)):
                return True
        return False


    def bfs(self, src, dst):
        if not src in self.graph.nodes or not dst in self.graph.nodes :
            return False
        nextToVisit = list()  # linkedlist
        visited = list()     # hashset
        nextToVisit.append(src)
        while len(nextToVisit) > 0:
            node = nextToVisit.pop()
            if node == dst:
                return True

            if node in visited:
                continue

            visited.append(node)

            for child in self.graph.getNode(node).adjacent:
                nextToVisit.append(child)
        return False

    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')

    graph = Graph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(2, 5)
    graph.addEdge(20, 50)

    print(GraphSearch(graph).dfs(1, 4))
    print(GraphSearch(graph).bfs(1, 4))

    