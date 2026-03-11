# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # 1. Find the rightmost node of the left subtree
                last = curr.left
                while last.right:
                    last = last.right
                
                # 2. Connect this rightmost node to the current right subtree
                last.right = curr.right
                
                # 3. Move the left subtree to the right
                curr.right = curr.left
                curr.left = None
            
            # 4. Move to the next node (which is now on the right)
            curr = curr.right