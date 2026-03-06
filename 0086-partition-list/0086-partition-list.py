# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Temporary dummy nodes to start our two chains
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to the current last node in each chain
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            
            curr = curr.next
            
        # Crucial: End the "after" list to avoid cycles
        after.next = None
        
        # Stitch the two lists together
        before.next = after_head.next
        
        return before_head.next