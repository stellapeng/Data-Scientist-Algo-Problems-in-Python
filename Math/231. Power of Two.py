# method 1: 
# bit manipulation: n & (n-1) == 0
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         if n < 1:
            return False
         return n & (n-1) == 0
        
# method 2:
# bit manipulation: n & (~n + 1) == n
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         if n < 1:
            return False
         return n & (~n + 1) == n


# method 3:
# Time Complexity: O(log(n))
# Space Complexity: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n%2 == 0:
            n /= 2
            
        return n == 1

    
# method 4:
# Time Complexity: O(1)
# Space Complexity: O(1)   
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       
        # to record all power of three under 2^31, there are 31 numbers in total
        ans = []  
        i = 1
        
        while i < 2147483648:
            ans.append(i)  
            i *= 2
        
        return n in ans

        