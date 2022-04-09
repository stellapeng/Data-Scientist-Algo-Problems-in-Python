# Time Complexisity: O(catalan nums growth rate)
# Time Complexisity: O(catalan nums growth rate)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def generator(self, low, high):
        res = [] # res need to be initilized within the function
        
        if low > high:
            res.append(None)
            return res
        
        for i in range(low, high+1):

            left_trees = self.generator(low, i - 1) # a list of all the possible left subtress roots
            right_trees = self.generator(i + 1, high) # a list of all the possible right subtress roots

            for lt in left_trees:
                for rt in right_trees:
                    root = TreeNode(i)
                    root.left = lt
                    root.right = rt
                    res.append(root)
            
        return res
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generator(1, n)
