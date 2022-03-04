# Two indices
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # keep all non-zero elements in front retaining the original order
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1       
        
        # adding zeros at the end making sure the length is the same with the 
        # orginal list
        for k in range(n-j):
            nums[j+k] = 0