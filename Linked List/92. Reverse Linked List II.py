# Time Complexity: O(n)
# Space Complexity: O(n)，this is the space occupied by the recursion stack. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.successor = ListNode(-1)
    
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # base case
        if (n == 1):
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n - 1)
        
        head.next.next = head
        head.next = self.successor
        
        return last
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if (left == 1):
            return self.reverseN(head, right);

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        
        return head
        
        
        