# Time Complexisity: O(nlogn) for sortings
# Space Complexisity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begin = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        n = len(intervals)
        
        overlap_cnt = 0
        mr_cnt = 1
        i, j = 0, 0
        
        while(i < n and j < n):
            if (begin[i] < end[j]):
                overlap_cnt += 1
                i += 1
            else:
                overlap_cnt -= 1
                j += 1
            mr_cnt = max(mr_cnt, overlap_cnt)
            
        return mr_cnt