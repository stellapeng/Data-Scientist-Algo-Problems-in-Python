# method 1: DP
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0] * n
        ans[0] = 1
        if n == 1:
            return ans[-1]
        ans[1] = 2
        if n == 2:
            return ans[-1]
        
        for i in range(2, n):
            ans[i] = ans[i-1] + ans[i-2]
        
        return ans[-1]
   

# method 2: Fibonacci Number
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
             return n
        
        n_1 = 1
        n_2 = 2
        for i in range(3, n+1):
            n_3 = n_1 + n_2
            n_1 = n_2
            n_2 = n_3
        
        return n_3



# method 3: Binets Method
# uses matrix multiplication to obtain the nth Fibonacci number
# q^(n+1) = np.matmul(q^n , np.array([[1, 1],[1, 0]]))
# Time Complexity: O(logn)
# Space Complexity: O(1)
import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        q = np.array([[1, 1],[1, 0]])
        res = q
        
        if n >= 2:
            for _ in range(n-1):
                # The numpy dot() function returns the dot product of two arrays. The result is the same as the matmul() function for one-dimensional and two-dimensional arrays.
                res = np.matmul(res, q) # or res = np.dot(res, q)
        return res[0][0]
    


# method 4: use close formula of getting the nth Fibonnacci number
# Time Complexity: O(logn), pow method takes logn time.
# Space Complexity: O(1)
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1+sqrt5)/2,n+1) - math.pow((1-sqrt5)/2,n+1)
        return int (fibn/sqrt5)



# method 5: Brute Force: TLE
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


