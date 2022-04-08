# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def traverse(self, root):
        if root is None:
            return None
        
        # traverse in descending order
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)

        return root
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.traverse(root)
        return root