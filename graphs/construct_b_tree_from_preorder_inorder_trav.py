#!/usr/bin/env python

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def buildTree(self, preorder, inorder):        

        def f(inorder):
            if inorder:         
                val = preorder.pop(0)
                i = inorder.index(val)
                bst = TreeNode(val)
                print("Call i={} val={} left={} right={}".format(i, val, inorder[:i], inorder[i+1:]))
                bst.left=f(inorder[:i])
                bst.right=f(inorder[i+1:])
                return bst       

        return f(inorder)




def print_nodes(node, prefix = "root -> "):            
    v = node.val
    if node.left:
        res = print_nodes(node.left, "P={} L -> ".format(v))
    print(prefix + str(node.val))
    if node.right:
        print_nodes(node.right, "P={} R -> ".format(v))

    return


preorder = [1,5,2,3,4]
inorder = [1,2,3,4,5]

s = Solution()

nodes=s.buildTree(preorder, inorder)

print_nodes(nodes)

