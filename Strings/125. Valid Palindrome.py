# method 1: two indices
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            
        return True


# method 2: 
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        
        w = [i.lower() for i in s if i.isalnum()]
        n = len(w)
        for i in range(n//2):
            if w[i] != w[n-1-i]:
                return False
        return True

    
# method 3: reversed list
# filter(function, iterable): Extract elements from an iterable (list, tuple..) for which a function returns True
# map(function, iterable): executes a specified function for each item in an iterable.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = filter(lambda c: c.isalnum(), s)
        lowercase_filtered_chars = map(lambda c: c.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list

