# method 1: most syntax-simple
# time complexity: O(n), , perform n//2 swaps
# space complexity: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) // 2
        
        for i in range(n):
            s[i], s[-i-1] = s[-i-1], s[i] 
            

            
# method 2: two index method, clearer in indexing
# time complexity: O(n), , perform n//2 swaps
# space complexity: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0,  len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left] 
            left, right = left + 1, right - 1
            
            
            
# method 3: use recursion
# time complexity: O(n), perform n//2 swaps
# space complexity: O(n) to keep recrusion stack    
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left] 
                helper(left + 1, right - 1)
        
        helper(0, len(s)-1)

        
# method 4: python built-in list in-place reverse function
# time complexity: O(n)
# note: s= s[::-1] wont work, it's not in-place reverse
class Solution:
    def reverseString(self, s):
        s.reverse()

                    
           