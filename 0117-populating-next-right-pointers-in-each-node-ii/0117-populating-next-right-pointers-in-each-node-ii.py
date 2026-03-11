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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root # Pointer for the level we are currently on
        
        while curr:
            # Dummy node to mark the start of the next level
            dummy = Node(0)
            tail = dummy # Pointer to build the next level's linked list
            
            # Traverse the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                # Move to the next node in the current level
                curr = curr.next
            
            # Move curr to the start of the next level we just built
            curr = dummy.next
            
        return root