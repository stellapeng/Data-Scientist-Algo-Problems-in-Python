# env: python
# Two pointers
# the dummy variable prehead is the tricky way to preserve the merged list head
# Time Complexity: O(nlogk) logk -> priority queue
# Space Complexity: O(n+k), n -> the new list, k -> priority queue

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    
        if (len(lists) == 0):
            return None
        
        prehead = ListNode(-1)
        zipper = prehead
        
        pq = PriorityQueue()

        for l in lists:
            if l:
                pq.put((l.val, l))
        
        while not pq.empty():
            value, node = pq.get()  
            zipper.next = ListNode(value)
            zipper = zipper.next
            node = node.next
            if node:
                pq.put((node.val, node))
        
        return prehead.next
    
    
