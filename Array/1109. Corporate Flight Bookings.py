# cache array diff
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        
        for l in bookings:
            i = l[0] - 1
            j = l[1] - 1
            val = l[2]
            
            diff[i] += val
            if j+1 <= n-1:
                diff[j+1] -= val
                
        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i-1] + diff[i]
        
        return res

    