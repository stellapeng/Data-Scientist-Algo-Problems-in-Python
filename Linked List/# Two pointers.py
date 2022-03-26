# Two pointers
# the dummy variable prehead is the tricky way to preserve the merged list head
# Time Complexity: O(m+n)
# Space Complexity: O(m+n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        n1 = list1
        n2 = list2
        
        prehead = ListNode(-1) # -1 can be omitted, the value is default by 0
        
        zipper = prehead
        
        while (n1 is not None and n2 is not None):
            if n1.val <= n2.val:
                zipper.next = n1
                n1 = n1.next
            else:
                zipper.next = n2
                n2 = n2.next
            zipper = zipper.next
        
        zipper.next = n1 if n1 is not None else n2
        
        return prehead.next

        