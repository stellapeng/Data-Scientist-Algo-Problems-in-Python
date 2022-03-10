class Solution:
    def myAtoi(self, input: str) -> int:
        sign = 1 
        result = 0
        index = 0
        n = len(input)
        
        # INT_MAX = pow(2,31) - 1 
        # INT_MIN = -pow(2,31)
        
        # we can manually put 2^31-1 and -2^31 here to get quicker calc
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        # skip leading spaces
        while index < n and input[index] == ' ':
            index += 1
        
        # determine sign once
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1
        
        # only check the following digits part
        # two ways to check if the character/string is a digit:
        ## 1. string.isdigit(), input[index].isdigit()
        ## 2. regex: re.match(), re.match(r'[0-9]', input[index])
        while index < n and re.match(r'[0-9]', input[index]): 
            digit = int(input[index])
            
             # Check overflow and underflow
            if ((result >INT_MAX//10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN
            
            # Append current digit to the result.
            result = 10 * result + digit
            index += 1
        
        return sign * result
            
            