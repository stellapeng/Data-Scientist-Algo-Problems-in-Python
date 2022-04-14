import sys 

class Solution:
    # from 172
    def trailingZeroes(self, n: int) -> int:
        divisor = 5
        res = 0
        while (divisor <= n):
            res += n // divisor
            divisor *= 5
        return res
    
    def preimageSizeFZF(self, k: int) -> int:
        return (self.right_bound(k) - self.left_bound(k) + 1)
    
    # binary search right bound
    def right_bound(self, k):
        low = 0
        high = sys.maxsize # 9,223,372,036,854,775,807
        while(low < high):
            mid = low + (high-low)//2
            if (self.trailingZeroes(mid) < k):
                low = mid + 1
            elif (self.trailingZeroes(mid) > k):
                high = mid
            else:
                low = mid + 1
        return (low - 1)
    
    # binary search left bound
    def left_bound(self, k):
        low = 0
        high = sys.maxsize
        while(low < high):
            mid = low + (high-low)//2
            if (self.trailingZeroes(mid) > k):
                high = mid
            elif (self.trailingZeroes(mid) < k):
                low = mid + 1
            else:
                high = mid
        return low
