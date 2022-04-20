# Reservoir sampling

# Time Complexisity: O(n)
# Space Complexisity: O(1)

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        n = len(self.nums)
        for i in range(n):
            if (self.nums[i] != target):
                continue

            # generate an int in [0, count)
            # the probabiity of being 0 is 1/count
            count += 1
            if (random.randint(0, count-1) == 0): # randint: both included
                res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)