class Solution:
    def preorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)   # Root
            dfs(node.left)         # Left
            dfs(node.right)        # Right

        dfs(root)
        return res