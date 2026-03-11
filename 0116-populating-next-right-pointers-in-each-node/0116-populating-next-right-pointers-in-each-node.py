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
        if not root:
            return root
        
        # Start with the root level
        leftmost = root
        
        # While there is a next level to connect
        while leftmost.left:
            # Iterate through the current level using 'next' pointers
            curr = leftmost
            while curr:
                # Connection 1: Same parent
                curr.left.next = curr.right
                
                # Connection 2: Different parents
                if curr.next:
                    curr.right.next = curr.next.left
                
                # Move to the next node in the current level
                curr = curr.next
            
            # Move down to the next level
            leftmost = leftmost.left
            
        return root