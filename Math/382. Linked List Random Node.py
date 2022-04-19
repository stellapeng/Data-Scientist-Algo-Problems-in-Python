# iterating twice is easy
# we can only iterate once to achieve the goal
# when encountering the ith element, the probability of picking it should be 1/i
# the probability of not picking is should be 1 - 1/i

# Time Complexisity: O(n)
# Space Complexisity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        r = random.random()
        n = self.head
        res = 0
        i = 0
        while(n):
            i += 1
            # generate an int in [0, i)
            # the probabiity of being 0 is 1/i
            if (random.randint(0, i-1) == 0): # randint: both included
                res = n.val
            n = n.next
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()