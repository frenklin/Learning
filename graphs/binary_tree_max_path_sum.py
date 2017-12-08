#!/usr/bin/env python


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxval=-100000
        
        def maxpath(root):
            if not root:
                return 0
            l=max(0,maxpath(root.left))
            r=max(0,maxpath(root.right))
            self.maxval=max(self.maxval,l+r+root.val)
            return root.val+max(l,r)
        
        maxpath(root)
        
        #print()
        return self.maxval



nodes = TreeNode(1)
nodes.left = TreeNode(2)
nodes.right = TreeNode(3)


s = Solution()

print(s.maxPathSum(nodes))