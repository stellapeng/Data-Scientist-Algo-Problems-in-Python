# method 1: dictionary
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            d[n] = 1
        
        return False



# method 2: dictionary
# Time complexity: O(nlog(n))
# Space complexity: O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # (nlog(n))

        for i, v in enumerate(nums[:-1]):
            if v == nums[i+1]:
                return True
        
        return False
            