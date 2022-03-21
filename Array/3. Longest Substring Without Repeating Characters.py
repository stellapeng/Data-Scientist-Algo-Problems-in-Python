# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = defaultdict(int)
        
        left, right = 0, 0
        res = 0
        
        while (right < len(s)):
            # move c to the window
            c = s[right]
            right += 1
            
            # ... UPDATE THE SLIDING WINDOW ... 
            window[c] += 1
               
            # if need to shrink the window 
            # while ([v for k, v in window.items() if v>1]) also works, but actually we only need to check window[d]
            while (window[c] > 1): 
                
                # moving d outside of the sliding window    
                d = s[left]
                left += 1
                
                # ... UPDATE THE SLIDING WINDOW ... 
                window[d] -= 1
            
            res = max(res, right - left)
                    
        return res
        
        