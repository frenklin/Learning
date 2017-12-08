#!/usr/bin/env python

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def buildTree(self, inorder, postorder):        

        def f(inorder):
            if inorder:         
                val = postorder.pop()
                i = inorder.index(val)
                bst = TreeNode(val)
                print("Call i={} val={} left={} right={}".format(i, val, inorder[:i], inorder[i+1:]))
                bst.right=f(inorder[i+1:])
                bst.left=f(inorder[:i])                
                return bst       

        return f(inorder)


#        indicies = {}
#        for index, elem in enumerate(inorder):
#            indicies[elem] = index
#        def helper(left_post, right_post, left_in, right_in):
#            if left_post > right_post or left_in > right_in:
#                return None
#            root = TreeNode(postorder[right_post])
#            root_index = indicies[postorder[right_post]]
#            root.left = helper(left_post, left_post + root_index - left_in - 1, left_in, root_index - 1)
#            root.right = helper(left_post + root_index - left_in, right_post - 1, root_index + 1, right_in)
#            return root
#
#         return helper(0, len(postorder) - 1, 0, len(inorder) - 1)
            


def print_nodes(node, prefix = "root -> "):            
    v = node.val
    if node.left:
        res = print_nodes(node.left, "P={} L -> ".format(v))
    print(prefix + str(node.val))
    if node.right:
        print_nodes(node.right, "P={} R -> ".format(v))

    return


inorder = [2,1,3]
postorder = [2,3,1]

s = Solution()

nodes=s.buildTree(inorder, postorder)

print_nodes(nodes)

