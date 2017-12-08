#!/usr/bin/env python
from queue import Queue
from threading import Thread


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):   
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        qnodes = Queue()
        results = Queue()
        qnodes.put((root, 1))
        for x in range(8): 
            worker = TreeNodeVisitorTask(qnodes, results)
            worker.daemon = True
            worker.start()

        qnodes.join()
        #result_val=0
        result_depth=0

        while not results.empty():
            val, depth = results.get()
            if depth > result_depth:
         #       result_val = val
                result_depth = depth
        
        return result_depth

# multithreaded solution doesn't work on leetcode
class TreeNodeVisitorTask(Thread):
    def __init__(self, qnodes, results):
        Thread.__init__(self)
        self.qnodes = qnodes
        self.results = results

    def run(self):
        while True:
            node, depth = self.qnodes.get()
            if not node is None:
                if node.left is None or node.right is None:
                    self.results.put((node.val, depth))
                if not node.left is None:
                    self.qnodes.put((node.left, depth + 1))
                if not node.right is None:
                    self.qnodes.put((node.right, depth + 1))
            self.qnodes.task_done()
        
 

nodes = TreeNode(1)
nodes.left = TreeNode(2)
nodes.right = TreeNode(3)
nodes.right.right = TreeNode(4)

s = Solution()

print(s.maxDepth(nodes))