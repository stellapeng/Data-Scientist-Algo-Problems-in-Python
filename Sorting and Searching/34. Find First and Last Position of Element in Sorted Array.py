# Time Complexisty: O(nlogn)
# Space Complexisty: O(1)

class Solution:
    
    def leftMost(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while (left <= right) :
            mid = left + (right - left)//2
            if (nums[mid] == target):  ## shrink the searching window from right to left
                right = mid - 1
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
        
        # when loop termintes, left = right + 1, check the edge case left = (len(nums) - 1) + 1
        if (left >= len(nums) or nums[left] != target):
            return -1
        
        return left

    
    def rightMost(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while (left <= right) :
            mid = left + (right - left)//2
            if (nums[mid] == target): ## shrink the searching window from left to right
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
        
        # when loop termintes, left = right + 1, check the edge case right = left - 1 = -1
        if (right <= -1 or nums[right] != target):
            return -1
        
        return right
    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftMost(nums, target), self.rightMost(nums, target)]
        