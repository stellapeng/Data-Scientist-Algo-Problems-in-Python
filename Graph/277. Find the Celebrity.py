
# Time Complexisty: O(n)
# Space Complexisty: O(1)

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for other in range(1, n):
            if (not knows(other, candidate) or knows(candidate, other)):
                candidate = other
                
        for other in range(n):
            if (candidate == other):
                continue
                
            if (not knows(other, candidate) or knows(candidate, other)):
                return -1
        
        return candidate
        