# we cannot just verity the root's left and right childs
# also need to verify if the left (right) subtree is smaller (larger) than the root's parent
# that's why we need to pass in additional parameters carrying the constraints (min and max bounds) to the entire subtree

# Time complexity: O(h), h is the height of the tree, h=logn for the rebalanced tree. O(logn) in the average case, and O(n) in the worst case.
# Space complexity: O(h) to keep the recursion stack, i.e. O(logn) in the average case, and O(n) in the worst case.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verifyBST(self, root, min_bound, max_bound):
        if (root is None):
            return True
        
        if (min_bound and root.val <= min_bound.val):
            return False
        if (max_bound and root.val >= max_bound.val):
            return False
        
        return (self.verifyBST(root.left, min_bound, root) and 
                self.verifyBST(root.right, root, max_bound))
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.verifyBST(root, None, None)
        