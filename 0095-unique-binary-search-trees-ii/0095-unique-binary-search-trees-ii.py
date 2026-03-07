# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int):
        
        if n == 0:
            return []
        
        def build(start, end):
            trees = []
            
            if start > end:
                trees.append(None)
                return trees
            
            for i in range(start, end + 1):
                
                leftTrees = build(start, i - 1)
                rightTrees = build(i + 1, end)
                
                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            
            return trees
        
        return build(1, n)