# Time Complexity: O(n)
# Space Complexity: O(n)

# Python built-in Lists are not Linked lists. They are variable size arrays.
# to implement monotoniQueue, we want to insert and pop from the back and front are O(1), linkedlist is O(1)
# deque is a sequence container with the ability of expansion and contraction on both ends.
# deque() is a python build-in library, it can act list linkedlist if we only need to insert to the back and pop from the front

# implement monotonicQueue as a class
class monotonicQueue:
    def __init__(self):
        self.q = deque()
    
    def push(self, n:int):
        while (self.q and self.q[-1] < n):
            self.q.pop()
        self.q.append(n)
    
    def max(self) -> int:
        return self.q[0];
    
    def pop(self, n:int):
        if n == self.q[0]:
            self.q.popleft()
    
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = monotonicQueue()
        
        for i in range(len(nums)):
            if i < k - 1:
                window.push(nums[i])

            else:
                # push
                window.push(nums[i])
    
                # add max to the result list
                res.append(window.max())
                
                # pop
                window.pop(nums[i-k+1])
                
        return res


# Just structured differently
# implement the monotomic queue within the main structure 
class Solution:
    def __init__(self):
        self.window = deque()
    
    def windowPush(self, n:int):
        while (self.window and self.window[-1] < n):
            self.window.pop()
        self.window.append(n)
               
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            if i < k - 1:
                self.windowPush(nums[i])

            else:
                # push
                self.windowPush(nums[i])
                
                # add max to the result list
                res.append(self.window[0])
                
                # pop
                if nums[i-k+1] == self.window[0]:
                    self.window.popleft()
                
        return res


