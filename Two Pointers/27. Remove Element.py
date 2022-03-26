# Time Complexisty: O(n)
# Space Complexisty: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        l = 0
        
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                l += 1
                
        return l
        