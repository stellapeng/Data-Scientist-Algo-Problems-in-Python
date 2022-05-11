class Solution(object):

    def backtrack(self, start, n, k, track, res):
        if (len(track) == k):
            # pass by reference, need to deep copy the path list before adding to result
            track_copy = [i for i in track] # or path.copy()
            res.append(track_copy)
            return;
        
        for i in range(start, n+1):
            track.append(i)
            self.backtrack(i+1, n, k,track, res)
            track.remove(i) # or track.pop()
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        track = []
        res = [] # or initialzie res as a class attribute
        self.backtrack(1, n, k, track, res)
        return res
        