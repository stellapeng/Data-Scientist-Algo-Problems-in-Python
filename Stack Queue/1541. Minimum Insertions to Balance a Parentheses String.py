# Time Complexisty: O(n)
# Space Complexity: O(1)

class Solution:
    def minInsertions(self, s: str) -> int:
        need = 0 # based on left, count the need for right
        res = 0 # times of adding left or right bracket
        for c in s:
            if c == '(':
                need += 2
                if need %2 ==1:
                    res += 1 # add a right
                    need -= 1 # reduce the need for right
                    
                
            elif c == ')':
                need -= 1
                
                if need == -1: # too many right
                    res += 1 # add a left
                    need = 1 # increase the need for right by adding 2
                    
        return need + res;

