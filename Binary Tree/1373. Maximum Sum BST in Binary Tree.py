# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = 0
        
    def traverse(self, root: Optional[TreeNode]) -> []:
        if root is None:
            # BST?, min, max, bst sum
            return [1, float('inf'), float('-inf'), 0]
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        res = [-1, -1, -1, -1]
        if (left[0] == 1 and right[0] == 1):
            if root.val > left[2] and root.val < right[1]:
                res[0] = 1
                res[1] = min(left[1], root.val)
                res[2] = max(right[2],root.val)
                res[3] = left[3] + right[3] + root.val
                self.maxSum = max(self.maxSum, res[3])
        else:
            res[0] = 0
        
        return res
    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxSum