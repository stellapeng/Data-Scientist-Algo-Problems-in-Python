class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')',
             '[': ']',
             '{': '}'}
        
        # list can mimic stack in python
        l = [] 
        for i in s:
            if i in d:
                l.append(i)
            elif l and i == d[l[-1]]:
                l.pop() 
            else:
                return False
        
        return not l