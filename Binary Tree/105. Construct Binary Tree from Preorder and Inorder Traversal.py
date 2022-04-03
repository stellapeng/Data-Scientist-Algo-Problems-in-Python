# Time complexity: O(n)
# Space complexity: O(n) 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root_value = preorder[0]
        root_idx = inorder.index(root_value)
        
        left_preorder = preorder[1:(root_idx+1)]
        right_preorder = preorder[(root_idx+1):]
        
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[(root_idx+1):]
        
        root = TreeNode(root_value)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root