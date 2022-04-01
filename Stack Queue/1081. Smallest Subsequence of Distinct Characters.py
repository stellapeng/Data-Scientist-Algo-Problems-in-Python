# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk = []
        inStack = [False]*256;
        
        count = [0]*256;
        for c in s:
            count[ord(c)] += 1
        
        for c in s:
            count[ord(c)] -= 1
            
            if inStack[ord(c)]:
                continue
                
            while stk and stk[-1] > c and count[ord(stk[-1])] > 0:
                inStack[ord(stk[-1])] = False
                stk.pop()
                
            stk.append(c)
            inStack[ord(c)] = True


        s = ''
        while (stk):
            s += stk.pop()

        return s[::-1]

