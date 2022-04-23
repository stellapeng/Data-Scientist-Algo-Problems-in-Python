from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        
        for i in nums:
            q.put(i)
            if q.qsize() > k:
                q.get()
        
        return q.get()