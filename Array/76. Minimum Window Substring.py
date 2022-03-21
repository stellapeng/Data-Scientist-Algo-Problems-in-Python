 # Time Complexity: O(n)
 # Space Complexity: O(1)
 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        
        left, right = 0, 0
        valid = 0
        
        length = float('inf')
        start = 0
        
        while (right < len(s)):
            # move c into the sliding window
            c = s[right]
            right += 1
            
            # ... UPDATE THE SLIDING WINDOW ... 
            if c in need:
                window[c] += 1 # or define window = {}, window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            # if need to shrink the window
            while (valid == len(need)):
                # update the minimum substring
                if right - left < length:
                    start = left
                    length = right - left
                
                # moving d outside of the sliding window
                d = s[left]
                left += 1
                
                # ... UPDATE THE SLIDING WINDOW ... 
                if d in need:           
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return '' if length == float('inf') else s[start:(start+length)]