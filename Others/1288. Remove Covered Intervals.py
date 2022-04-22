# Time complexity: O(nlogn), dominated by sorting
# Space complexity: O(n) or O(logn), depends on sorting implementation

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # two keys sorting:
        # key 1: ascending by interval lower bounds
        # key 2: descending by interval upper bounds
        # this garantees intervals[0] wont be covered by any other intervals
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        nint = len(intervals)
        
        left = intervals[0][0]
        right = intervals[0][1]
        cover_cnt = 0
        for i in range(1, nint):
            sub_int = intervals[i]
            # case 1: found covered interval
            if sub_int[0] >= left and sub_int[1] <= right:
                cover_cnt+=1
                
            # case 2: overlapped intervals, construct a wider  one
            if sub_int[0] >= left and sub_int[1] > right: 
                right = sub_int[1]
                
            # case 3: completely disjoined, update left and right
            if sub_int[0] >= right:
                left = sub_int[0]
                right = sub_int[1]
                
        return nint - cover_cnt