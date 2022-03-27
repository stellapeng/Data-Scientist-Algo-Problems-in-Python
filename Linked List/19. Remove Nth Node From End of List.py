# Time Complexity: O(n), one pass, n
# Space Complexity: O(1),

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head 
        for _ in range(n):
            p1 = p1.next
        
        p2 = head
        
        while (p1 is not None): # or: p1 != None   both are valid syntax
            p1 = p1.next
            p2 = p2.next
        
        return p2
            
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list.
        prehead = ListNode(-1)
        prehead.next = head
    
        pre_delete = self.findFromEnd(prehead, n+1)
        pre_delete.next = pre_delete.next.next
        
        return prehead.next
        
            
