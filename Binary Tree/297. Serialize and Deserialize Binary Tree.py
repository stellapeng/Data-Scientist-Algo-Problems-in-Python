# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# pre-order
class Codec:
    def __init__(self):
        self.sb = ''

    def s_helper(self, root):
        if root is None:
            self.sb += 'None,'
            return
        
        self.sb += str(root.val)
        self.sb += ','
        self.s_helper(root.left)
        self.s_helper(root.right)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.s_helper(root);
        return self.sb
        
        
    def ds_helper(self, data_list):
        
        if not data_list:
            return None
        
        if data_list[0] == 'None':
            data_list.pop(0)
            return None
        
        root = TreeNode(int(data_list[0]))
        data_list.pop(0)
        
        root.left = self.ds_helper(data_list)
        root.right = self.ds_helper(data_list)
        
        return root
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        
        return self.ds_helper(data_list)
        
        
# post-order       
class Codec:
    def __init__(self):
        self.sb = ''

    def s_helper(self, root):
        
        if root is None:
            self.sb += 'None,'
            return

        self.s_helper(root.left)
        self.s_helper(root.right)
        
        self.sb += str(root.val)
        self.sb += ','
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.s_helper(root);
        return self.sb
        
        
    def ds_helper(self, data_list):
        
        if not data_list:
            return None
        
        if data_list[-1] == 'None':
            data_list.pop()
            return None
        
        last = data_list.pop()
        root = TreeNode(int(last))
        
        root.right = self.ds_helper(data_list)
        root.left = self.ds_helper(data_list)
        
        return root
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")[:-1]

        return self.ds_helper(data_list)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

