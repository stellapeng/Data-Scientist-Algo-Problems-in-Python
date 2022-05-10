class Solution: 
    def __init__(self):
        self.res = []
        
    def backtrack(self, nums, track, used):
        if (len(track) == len(nums)):
            # pass by reference, need to deep copy the path list before adding to result
            track_copy = [i for i in track] # or track.copy()
            self.res.append(track_copy)
            return;
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            track.append(nums[i])
            used[i] = True
            self.backtrack(nums, track, used)
            track.remove(nums[i])
            used[i] = False
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums) 
        self.backtrack(nums, track, used)
        return self.res