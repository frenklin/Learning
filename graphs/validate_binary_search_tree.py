#!/usr/bin/env python


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """             
        def f():
            stack=[root]
            res=-99999999999999
            while stack:
                curr=stack.pop()
                if curr:
                    stack.append(curr)
                    stack.append(curr.left)
                else:
                    if stack:
                        curr=stack.pop()
                        if res > curr.val:
                            return False
                        res = curr.val
                        stack.append(curr.right)
            return True

        def f2(root): 
            if not root:
                 return True
            stack = []
            pre = None
            while root or len(stack)>0:
                while root:
                    stack.append(root)
                    root = root.left                
                root = stack.pop()
                if pre and root.val <= pre.val:
                    return False
                pre = root
                root = root.right
            
            return True
            
            
        return f2(root)



n = TreeNode(2)

n.right = TreeNode(3)

n.left = TreeNode(1)

s = Solution()

print(s.isValidBST(n))