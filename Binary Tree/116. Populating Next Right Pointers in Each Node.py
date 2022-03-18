"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        self.connectTwoNode(root.left, root.right)
        
        return root
        
    def connectTwoNode(self, n1:'Node', n2:'Node') -> 'None':
        if n1 is None and n2 is None:
            return 
        

        # pre-order traverse: root, left, right 
        n1.next = n2
        
        # connect the children from the same parent: left, right
        self.connectTwoNode(n1.left, n1.right)
        self.connectTwoNode(n2.left, n2.right)
        
        # cross connect the right child of n1 with the left child of n2
        self.connectTwoNode(n1.right, n2.left)

        # note: the connection order does not really matter