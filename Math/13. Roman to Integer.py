class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"M": 1000,
             "D": 500,
             "C": 100,
             "L": 50,
             "X": 10,
             "V": 5,
             "I": 1}
        
        ans = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1 or d[s[i]] >= d[s[i+1]]:
                ans += d[s[i]]
                i += 1
            else:
                ans += d[s[i+1]] - d[s[i]]
                i += 2

        return ans



class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"M": 1000,
             "D": 500,
             "C": 100,
             "L": 50,
             "X": 10,
             "V": 5,
             "I": 1,
             "CM": 900,
             "CD": 400,
             "XC": 90,
             "XL": 40,
             "IX": 9,
             "IV": 4}

        ans = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in d:
                ans += d[s[i:i+2]] 
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans