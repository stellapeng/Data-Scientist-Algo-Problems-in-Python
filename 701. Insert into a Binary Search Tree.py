# insertion to a BST always happens to the leafs
# Time complexity: O(h), h is the height of the tree, O(logn) in the average case, and O(n) in the worst case.
# Space complexity: O(h) to keep the recursion stack, i.e. O(logn) in the average case, and O(n) in the worst case.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root is None):
            return TreeNode(val)
        
        if (val < root.val):
            root.left = self.insertIntoBST(root.left, val)
        if (val > root.val):
            root.right = self.insertIntoBST(root.right, val)
            
        return root
