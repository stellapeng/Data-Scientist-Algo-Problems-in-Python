# Space: O(n*logm), n is the length of weights, m is the maximum capacity we tried
# Space Complexity: o(1)

class Solution:
    def f(self,  weights: List[int], capacity: int) -> int:
        days_needed = 0 
        each_batch = 0
        for i in weights:
            if each_batch + i > capacity:
                each_batch = i
                days_needed += 1
            else:
                each_batch += i
        return days_needed + 1
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # x: weight capacity of the ship
        # f(x): days needed
        # target: days
        
        # minimum possible capacity = max(weights)
        # maximum possible capacity = sum(weights)
        left, right = max(weights), sum(weights)
        
        while (left < right):
            mid = left + (right - left) // 2
            if (self.f(weights, mid) <= days):
                right = mid
            else:
                left = mid + 1
        
        return left