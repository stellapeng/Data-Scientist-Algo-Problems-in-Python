# divide and conquer

# Time complexity: all possible precedence: catalan numbers

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                left = expression[:i]
                right = expression[(i+1):]
                res_left = self.diffWaysToCompute(left)
                res_right = self.diffWaysToCompute(right)
                
                for l in res_left:
                    for r in res_right:
                        if expression[i] == '+':
                            res.append(int(l)+int(r))
                        elif expression[i] == '-':
                            res.append(int(l)-int(r))
                        elif expression[i] == '*':
                            res.append(int(l)*int(r))
                
        if not res:
            res.append(int(expression))
            
        return res