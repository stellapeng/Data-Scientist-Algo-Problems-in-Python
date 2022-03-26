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
        slow = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1       
        
        # adding zeros at the end making sure the length is the same with the 
        # orginal list
        while(slow < len(nums)):
            nums[slow] = 0
            slow += 1
            

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1
        