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
        self.res = set()
        self.subtrees = defaultdict(int)
        
    def helper(self, root: Optional[TreeNode]) -> string:
        if root is None:
            return "None"
        
        left_str = self.helper(root.left)
        right_str = self.helper(root.right)
        
        subtree_str = left_str + ',' + right_str + ','  + str(root.val)
        
        self.subtrees[subtree_str] += 1
        
        if self.subtrees[subtree_str] == 2:
            self.res.add(root)
        
        return subtree_str
            
        
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.helper(root)
        
        return self.res

