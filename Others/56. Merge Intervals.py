# Time complexity: O(nlogn), dominated by sorting
# Space complexity: O(n) or O(logn), depends on sorting implementation

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # two keys sorting:
        # key 1: ascending by interval lower bounds
        # key 2: descending by interval upper bounds
        # this garantees intervals[0] wont be covered by any other intervals
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        nint = len(intervals)
        res = [intervals[0]]
        
        for i in range(1, nint):
            sub_int = intervals[i]
            last = res[-1]
            if last[1] >= sub_int[0]:
                res[-1][1] = max(last[1], sub_int[1])
            
            if last[1] < sub_int[0]:
                res.append(sub_int)

                
        return res