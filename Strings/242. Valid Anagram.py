# method 1: sort()
# covert string to list, then sort the lists to compare
# Time Complexity: O(nlog(n))
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ls = list(s)
        lt = list(t)
        
        ls.sort()
        lt.sort()
        
        return True if ls == lt else False


# method 2: dictionary or hash table or counter
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        # iteratble collections can be passed to Collection.Counter, including string, list
        ls = Counter(s)  
        lt = Counter(t)

        return True if ls == lt else False
