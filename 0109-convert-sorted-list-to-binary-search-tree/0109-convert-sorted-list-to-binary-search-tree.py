class Solution:
    def sortedListToBST(self, head):
        
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        # find middle
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # cut left half
        if prev:
            prev.next = None
        
        root = TreeNode(slow.val)
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root