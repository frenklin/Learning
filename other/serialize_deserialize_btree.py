# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        def recursive_serialize(node):
            val = node.val            
            left = recursive_serialize(node.left) if node.left else ''
            right = recursive_serialize(node.right) if node.right else ''            
            return "{}:[{},{}]".format(val, left, right).replace(":[,]","")        

        return recursive_serialize(root)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None    

        def f(sub_data): 
            if sub_data:
                childs_index_separator = sub_data.find(':')                                              
                val = sub_data[:childs_index_separator] if childs_index_separator > -1 else sub_data.rstrip(']')                
                node = TreeNode(val) if len(val) > 0 else None
                right_node_index = childs_index_separator+1
                bracket_count = 0
                while True:
                    right_node_index += 1
                    if len(sub_data) < right_node_index+1:
                        return node
                    if sub_data[right_node_index] == ']':
                        bracket_count -= 1
                    elif sub_data[right_node_index] == '[':
                        bracket_count += 1
                    if bracket_count == 0 and sub_data[right_node_index] == ',':
                        break
                node.left = f(sub_data[childs_index_separator+2:right_node_index])                # skip :[                                                                
                node.right = f(sub_data[right_node_index:].lstrip('],'))
                return node
            else:
                return None
                
        
        return f(data)
        

root_node = TreeNode(1)
root_node.left = TreeNode(2)
root_node.left.left = TreeNode(12)
root_node.right = TreeNode(3)
root_node.right.left = TreeNode(44)
root_node.right.right = TreeNode(4)


c = Codec()
data = c.serialize(root_node)
#print(data)

new_root = c.deserialize(data)


def print_nodes(node):
    if node:
        print(node.val)
        print_nodes(node.left)        
        print_nodes(node.right)


print_nodes(new_root)




'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # a better solution with itertor with recursive method
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        else:
            return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return None
        vals = iter(data.split(','))
        root = self.helper(vals)
        return root
    
    def helper(self, vals):
        v = next(vals)
        if v == '#':
            return None
        else:
            root = TreeNode(v)
            root.left = self.helper(vals)
            root.right = self.helper(vals)
        return root

'''