# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Add current node to the path
            current_path.append(node.val)
            
            # Check if it's a leaf node and the sum matches
            if not node.left and not node.right and node.val == current_sum:
                result.append(list(current_path)) # Append a copy of the path
            else:
                # Continue DFS on children
                dfs(node.left, current_path, current_sum - node.val)
                dfs(node.right, current_path, current_sum - node.val)
            
            # Backtrack: remove the current node before going back up the tree
            current_path.pop()

        dfs(root, [], targetSum)
        return result