# approach 4: https://leetcode.com/problems/subarray-sum-equals-k/solution/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = defaultdict(int) # default value is int default: 0
        preSum[0] = 1

        ans = 0
        s = 0
        
        for i in range(1, len(nums)+1):
            s += nums[i-1]
            if s - k in preSum:
                ans += preSum[s-k]
                
            preSum[s] = preSum[s] + 1

        return ans

        