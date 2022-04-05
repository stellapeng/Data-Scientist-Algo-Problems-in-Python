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
        


# by layers
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ''
        
        if root is None:
            return s
        
        q = [root]
    
        while (q):
            cur = q[0]
            q.pop(0)
            if cur is None:
                s += "None,"
                continue
            s += str(cur.val)
            s += ','
            q.append(cur.left)
            q.append(cur.right)
        
        return s
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")[:-1]
        
        if not data_list:
            return None
        
        root = TreeNode(data_list[0])
        
        q = [root]
        
        i = 1
        while (i < len(data_list)):
            parent = q.pop(0)
            
            left_value = data_list[i]
            i+=1
           
            if left_value != 'None':
                parent.left = TreeNode(left_value)
                q.append(parent.left)
            else:
                parent.left = None
            
            right_value = data_list[i]
            i+=1
            if right_value != 'None':
                parent.right = TreeNode(right_value)
                q.append(parent.right)
            else:
                parent.right = None
                
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

