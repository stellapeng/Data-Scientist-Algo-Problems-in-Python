# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        s = 0
        mins = 0
        min_idx = 0
        for i in range(n):
            s += gas[i] - cost[i]
            if s < mins:
                mins = s
                # the min sum index is i, the start position is i+1
                min_idx = i + 1
        if s < 0:
            return -1
        else:
            return 0 if min_idx == n else min_idx
        