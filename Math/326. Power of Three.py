# method 1:
# Time Complexity: O(log(n))
# Space Complexity: O(1)
class Solution: 
    def isPowerOfThree(self, n: int) -> bool:        
        if n <= 0:
            return False
        if n == 1:
            return True
        tmp = 3
        while( tmp <= n ):
            if tmp == n:
                return True
            tmp *= 3
        return False


# method 2:
# Time Complexity: O(log(n))
# Space Complexity: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n%3 == 0:
            n /= 3
            
        return n == 1
    
    
# method 3:
# Time Complexity: O(1)
# Space Complexity: O(1)   
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
       
        # to record all power of three under 2^31, there are 20 numbers in total
        ans = []  
        i = 1
        while i < 2147483648:
            ans.append(i)  
            i *= 3

        return n in ans

    
    


