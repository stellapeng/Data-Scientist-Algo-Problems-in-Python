# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        freq = Counter(nums)
        need = defaultdict(int)
        
        for v in nums:
            if freq[v] == 0:
                continue
            
            if need[v] > 0:
                freq[v]-= 1
                need[v]-= 1
                need[v+1] += 1
            elif (freq[v] > 0 and freq[v+1] > 0 and freq[v+2] > 0):
                freq[v] -= 1
                freq[v+1] -= 1
                freq[v+2] -= 1
                need[v+3] += 1
            else:
                return False
            
        return True
        