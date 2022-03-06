# method 1.1: 
# bit manipulation: 
# n & (n-1) == 0 is the power of 2
# (101010...10)2 = (aaaaaaaa)16 , n & 0xaaaaaaaa == 0, is the power of 4 if it's a power of 2
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
         if n < 1:
            return False
         return (n & (n-1) == 0) and (n & 0xaaaaaaaa == 0)
        
# method 1.2: 
# bit manipulation: 
# (010101...01)2 = (55555555)16
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
         if n < 1:
            return False
         return (n & (n-1) == 0) and (n & 0x55555555 != 0)


# method 3:
# Time Complexity: O(log(n))
# Space Complexity: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n%2 == 0:
            n /= 4
            
        return n == 1

    
# method 4:
# Time Complexity: O(1)
# Space Complexity: O(1)   
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        # to record all power of three under 2^31, there are 16 numbers in total
        ans = []  
        i = 1
        
        while i < 2147483648:
            ans.append(i)  
            i *= 4
        
        return n in ans

        