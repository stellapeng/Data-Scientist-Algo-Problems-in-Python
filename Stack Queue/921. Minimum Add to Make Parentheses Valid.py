# Time Complexisty: O(n)
# Space Complexity: O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0 # based on left, count the need for right
        res = 0 # times of adding left bracket
        for c in s:
            if c == '(':
                need += 1
            
            elif c == ')':
                need -= 1
                
                if need == -1:
                    res += 1 # insert '('
                    need = 0
                    
        return need + res;

