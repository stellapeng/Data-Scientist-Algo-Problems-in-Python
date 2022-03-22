# Time Complexisty: O(nlogn)
# Space Complexisty: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while (right >= left):
            mid = left + (right - left)//2
            
            if (nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] < target):
                left = mid + 1 
    
        return -1