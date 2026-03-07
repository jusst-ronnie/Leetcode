class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # move prev to node before left
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # reverse nodes
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next