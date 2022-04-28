# same solution for 227 and 772

# Time Complexisty: O(n)
# Space Complexisty: O(n)

class Solution:
    def helper(self, s):
        sign = '+'
        stk = []
        num = 0
        while len(s) > 0:
            c = s.popleft()
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c == '(':
                num = self.helper(s)
                
            if (not c.isdigit() and c != ' ') or (len(s)==0):
                if sign == '+':
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                elif sign == '*':
                    stk[-1] = stk[-1] * num
                elif sign == '/':
                    stk[-1] = int(stk[-1] / float(num))                    
                num = 0
                sign = c
                
            if c == ')': 
                break

        return sum(stk)
                    
    
    def calculate(self, s: str) -> int:
        return self.helper(collections.deque(s))
        
   