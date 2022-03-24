# Time Space: O(n*logm), n is the length of pile, m is the maximum speed we tried
# Space Complexity: o(1)

class Solution:
    def f(self, piles: List[int], speed: int) -> int:
        hours = 0
        for i in piles:
            hours += math.ceil(i / speed)
        return hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1e9
        
        while (left < right):
            mid = left +  (right - left)//2
            if (self.f(piles, mid) <= h):
                right = mid 
            else:
                left = mid + 1
        
        return int(left)
                
            
## note: an application of binary search
# x is eating speed
# f(x) is the hours needed
# target is h 

