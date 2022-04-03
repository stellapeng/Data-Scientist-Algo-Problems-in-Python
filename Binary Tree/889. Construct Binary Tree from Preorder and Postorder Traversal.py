# Time complexity: O(n)
# Space complexity: O(n) 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root_value = preorder[0]
        left_root_value = preorder[1]
        root_idx_postorder = postorder.index(left_root_value)
        
        left_preorder = preorder[1:(root_idx_postorder+2)]
        right_preorder = preorder[(root_idx_postorder+2):]
        
        left_postorder = postorder[:(root_idx_postorder+1)]
        right_postorder = postorder[(root_idx_postorder+1):-1]
        
        root = TreeNode(root_value)
        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)
        
        return root