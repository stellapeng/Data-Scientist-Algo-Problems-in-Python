# two method to reverse the integer
# note to check overflow when reversing

# method 1: 
# reverse integer by modulo

class Solution:
    def reverse(self, x: int) -> int:
  
        flag = False
        if x < 0:
            flag = True   
            x = -x

        ans = 0
        m = x % 10
        while  x != 0:
            m = x % 10
            ans = ans * 10 + m
            
            # Check for the Reverse if it overflows. Remember that Our question condition is 
            # that our reverse should also be a 32-bit integer. If the reverse is not a 32-bit 
            # integer we should return 0.
            if(ans >= 2147483647 or ans <= -2147483647): # overflow if ans is outside of [-2^31, 2^31-1]
                print("WARNING OVERFLOWED!!!")
                return 0
            x = x // 10
        
        if flag:
            ans = -1*ans
            
        return ans
 

     
# method 2.1:
# converse to string, then reverse, converse back to int
# need to check overflow as well

class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True   
            x = -x
        
        ans = int(str(x)[::-1])   ## or use list.reverse()
        ans = -ans if flag else ans
        
        if(ans >= 2147483647 or ans <= -2147483647): # overflow if ans is outside of [-2^31, 2^31-1]
            print("WARNING OVERFLOWED!!!")
            return 0
        else:
            return ans



# method 2.2:
# convert to list of strings        
class Solution:
    def reverse(self, x: int) -> int:
        def reverseString(s: List[str]) -> None:
            n = len(s) // 2
            for i in range(n):
                s[i], s[-i-1] = s[-i-1], s[i] 
        
        flag = False
        if x < 0:
            flag = True   
            x = -x
        
        x_l = list(str(x))  ## conver '123' to ['1', '2', '3']
        reverseString(x_l)  ## or use built-in reverse method: x_l.reverse()
        ans = -int(''.join(x_l)) if flag else int(''.join(x_l))

        if(ans >= 2147483647 or ans <= -2147483647): # overflow if ans is outside of [-2^31, 2^31-1]
            print("WARNING OVERFLOWED!!!")
            return 0
        else:
            return ans
        

