# Time complexity: O(n)
# Space complexity: O(n) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        root_value = postorder[-1]
        root_idx = inorder.index(root_value)
        
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[(root_idx+1):]
        
        left_postorder = postorder[:root_idx]
        right_postorder = postorder[(root_idx):-1]
        
        root = TreeNode(root_value)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        
        return root
    
    