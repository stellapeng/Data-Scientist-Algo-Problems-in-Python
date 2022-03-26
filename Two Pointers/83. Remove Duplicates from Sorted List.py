# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexisty: O(n)
# Space Complexisty: O(1)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        
        if current_node is None:
            return head
        
        while (current_node.next is not None):
            if current_node.val == current_node.next.val:
                temp = current_node.next.next
                current_node.next = temp
            else:
                current_node = current_node.next
        return head 


# Time Complexisty: O(n)
# Space Complexisty: O(1)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        slow = head
        fast = head
        
        while (fast is not None):
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            else:
                fast = fast.next
        
        slow.next = None
        return head 


