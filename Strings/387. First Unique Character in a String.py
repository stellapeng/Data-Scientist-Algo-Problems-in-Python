# method 1: Collections.counter() 
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        cnter = Counter(s)   # O(n)
        
        for i, c in enumerate(s):  # O(n)
            if cnter[c] == 1:
                return i
            
        return -1


# method = 2: 
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            print(c)
            if c in d:
                d[c] = -1
            else:
                d[c] = i
                        
        ans = [v for k, v in d.items() if v != -1]
        
        return ans[0] if ans else -1
            
      