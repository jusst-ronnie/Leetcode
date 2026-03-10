class Solution:
    def postorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)      # Left
            dfs(node.right)     # Right
            res.append(node.val) # Root

        dfs(root)
        return res