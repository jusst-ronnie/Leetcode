class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {v:i for i,v in enumerate(inorder)}
        self.post_index = len(postorder) - 1
        
        def helper(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_index]
            self.post_index -= 1
            
            root = TreeNode(root_val)
            
            index = inorder_map[root_val]
            
            # build right first
            root.right = helper(index+1, right)
            root.left = helper(left, index-1)
            
            return root
        
        return helper(0, len(inorder)-1)