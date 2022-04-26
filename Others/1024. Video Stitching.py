# Time Complexity: O(nlog), dominated by sort
# Space Complexity: O(1)


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips, key=lambda x: (x[0], -x[1]))
        
        curr_end = 0
        next_end = 0
        cnt = 0
        possible = False
        
        i = 0
        n = len(clips)
        while (i < n and curr_end >= clips[i][0]):
            while (i < n and curr_end >= clips[i][0]):
                next_end = max(next_end, clips[i][1])
                i += 1
                
            cnt += 1
            curr_end = next_end
            
            if curr_end >= time:
                return cnt
        
        return -1