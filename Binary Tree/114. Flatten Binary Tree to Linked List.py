# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
       
        """post-order traverse: left, right, root"""

        ## left, right
        # flattern left child tree, and right child tree
        self.flatten(root.left)
        self.flatten(root.right)
        
        ## root
        # move the flattened left child tree to the root right
        left = root.left
        right = root.right
        
        root.left = None
        root.right = left
        
        # move the flattened right child tree to the end of the left child tree
        n = root
        while n.right:
            n = n.right
        n.right = right