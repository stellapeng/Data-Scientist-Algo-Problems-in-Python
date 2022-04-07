# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.length_max = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_max = self.maxDepth(root.left) 
        right_max = self.maxDepth(root.right)
        
        self.length_max = max(self.length_max, left_max + right_max)
        
        return max(left_max, right_max) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth(root)
        return self.length_max
     