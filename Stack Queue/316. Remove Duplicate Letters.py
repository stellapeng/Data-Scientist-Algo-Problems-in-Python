# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        inStack = [False]*256;
        
        count = [0] * 256
        for c in s:
            count[ord(c)] += 1 # The function ord() gets the int value of the char.
    
        for c in s: 
            count[ord(c)] -= 1
            if (inStack[ord(c)]):
                continue;
            while (stk and stk[-1] > c):
                if (count[ord(stk[-1])] == 0):
                    break
                inStack[ord(stk.pop())] = False

            stk.append(c)
            inStack[ord(c)] = True


        s = ''
        while (stk):
            s += stk.pop()

        return s[::-1]

        