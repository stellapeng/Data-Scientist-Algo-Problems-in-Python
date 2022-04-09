# Time complexity: O(h), h is the height of the tree, h=logn for the rebalanced tree. O(logn) in the average case, and O(n) in the worst case.
# Space complexity: O(h) to keep the recursion stack, i.e. O(logn) in the average case, and O(n) in the worst case.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMin(self, root):

        while (root.left):
            root = root.left
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if (root is None):
            return None
        
        if (root.val == key):
            # target has no or one leaf
            if (root.left is None):
                return root.right
            
            if (root.right is None):
                return root.left
            
            # target has two leafs
            if (root.left is not None and root.right is not None):
                # the best practice is to replace the root Node, not just replace the root.val
                minNode = self.getMin(root.right)
                
                # recall what deleteNone() returns - the tree root node
                root.right = self.deleteNode(root.right, minNode.val)
                minNode.left = root.left
                minNode.right = root.right
                root = minNode

        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        
        return root
                
                