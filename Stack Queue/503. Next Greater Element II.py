# Time Complexity: O(n)
# each element in nums2 is pushed once and poped once

# Space Complexity: O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [-1] * n
        s = []
        
        for i in range(2*n-1, -1, -1):
            while (s and s[-1] <= nums[i%n]):
                s.pop()
            
            res[i%n] = s[-1] if s else -1
            s.append(nums[i%n])

        return res

