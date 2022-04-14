# Time Complexisty: O(logn)
# Time Complexisty: O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        divisor = 5
        res = 0
        while (divisor <= n):
            res += n // divisor
            divisor *= 5
        
        return res