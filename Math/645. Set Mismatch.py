# Time Complexity: O(n)
# Space Complexity: O(1)


# link index with element value, the dup index is the dup value
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                dup = abs(nums[i])
            else:
                nums[idx] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                missing = i+1
        return [dup, missing]




# Time Complexity: O(nlogn)
# Space Complexity: O(logn)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dup = -1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup = nums[i]
                break
        
        missing = int( (len(nums)+1)*len(nums)/2 - sum(nums) + dup)
        return [dup, missing]