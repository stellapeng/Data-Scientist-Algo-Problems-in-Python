# method 1: Gauss' Formula
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        return int (n*(n+1)/2 - s)


# method 1: sort
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if nums[-1] != n:
            return n
        if nums[0] != 0:
            return 0
        
        for i in range(n - 1):
            if nums[i+1] - nums[i] > 1:
                return i+1



# method 3: Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i



# method 4: Bit Manipulaton: XOR with the index
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    

