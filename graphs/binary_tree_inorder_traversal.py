#!/usr/bin/env python
# runtime O(n)
# space stack(max depth) + result (can be in stream)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def f(node): # recursive
            if node is None:
                return []            
            r = [] + f(node.left) + [node.val] + f(node.right)                        
            return r
        
        def f2(): # iterative
            stack=[root]
            res=[]
            while stack:
                curr=stack.pop()
                if curr:
                    stack.append(curr)
                    stack.append(curr.left)
                else:
                    if stack:
                        curr=stack.pop()
                        res.append(curr.val)
                        stack.append(curr.right)
            return res
            
        return f2()



n = TreeNode(1)

n.right = TreeNode(2)

n.right.left = TreeNode(3)

s = Solution()

print(s.inorderTraversal(n))