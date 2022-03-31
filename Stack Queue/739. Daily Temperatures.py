# Time Complexity: O(n)
# each element in nums2 is pushed once and poped once

# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [-1] * len(temperatures)
        s = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            while (s and temperatures[s[-1]] <= temperatures[i]):
                s.pop()
            
            res[i] = s[-1] - i if s else 0
            
            s.append(i)
        
        return res