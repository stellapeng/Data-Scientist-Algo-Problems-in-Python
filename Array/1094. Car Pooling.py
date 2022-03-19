# cache array diff
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # n = 0
        # for t in trips:
        #     n = max(n, t[2])

        n = 1000 # upper bound of trips is given
            
        diff = [0] * n
        for t in trips:
            i = t[1]
            j = t[2] - 1
            val = t[0]
            
            diff[i] += val
            if j+1 <= n-1:
                diff[j+1] -= val
        
        res = []
        for i, v in enumerate(diff):
            if i == 0:
                res.append(v)
            else:
                res.append(res[i-1] + v)
            
            if res[i] > capacity:
                return False
        
        return True

