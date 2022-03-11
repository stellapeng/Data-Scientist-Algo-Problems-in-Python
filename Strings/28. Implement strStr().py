# Time Complexity: O(n*m)
# Space Complexity: O(n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # Length of the needle
        n = len(needle)
        
        # Loop through the haystack and slide the window
        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1



# str.find(str, beg=0, end=len(string))
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)