# Time complexity: O(n^2)
# Space complexity: O(n)

# without helper function:

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        max_value = max(nums)
        max_idx = nums.index(max_value)
        
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        
        return root
    


# with helper function:

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        max_value = max(nums)
        max_idx = nums.index(max_value)
        
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        
        return root
    
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:    
    def helper(self, nums: List[int], low: int, high: int)-> Optional[TreeNode]:
        if low > high:
            return None
        
        max_value = nums[low]
        max_idx = low
        for i in range(low, high+1, 1):
            if nums[i] > max_value:
                max_value = nums[i]
                max_idx = i
            
        root = TreeNode(max_value)
        root.left = self.helper(nums, low, max_idx-1)
        root.right = self.helper(nums, max_idx+1, high)
        
        return root
