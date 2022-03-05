# use Binary search
# Time Complexity: O(log(n))
# Space Complexity: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n 
        while right > left:
            
            # should not use (left + right) // 2 to prevernt overflow
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
           
        return left