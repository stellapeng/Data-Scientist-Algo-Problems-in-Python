 # Time Complexity: O(n)
 # Space Complexity: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = defaultdict(int)
        
        left, right = 0, 0
        valid = 0
        
        while (right < len(s2)):
            # move c to the window
            c = s2[right]
            right += 1
            
            # ... UPDATE THE SLIDING WINDOW ... 
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid +=1
           
            # if need to shrink the window 
            while (right - left >= len(s1)):
                
                if valid == len(need):
                    return True
                
                # moving d outside of the sliding window    
                d = s2[left]
                left += 1
                
                # ... UPDATE THE SLIDING WINDOW ... 
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return False
            
        