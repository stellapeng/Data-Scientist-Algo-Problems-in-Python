# Time Complexisty: O(n)
# Space Complexity: O(height), O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method 1:
# pre-order: root, left, right
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
          
        return root


# method 2:
# post-order: left, right, root
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
          
        return root

# cannot place in in-order: left, root, right