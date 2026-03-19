class TrieNode:
    def __init__(self):
        self.children = [None, None]   # instead of dict

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        
        # build trie
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        max_xor = 0
        
        # find max xor
        for num in nums:
            node = root
            curr_xor = 0
            
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opposite = 1 - bit
                
                if node.children[opposite]:
                    curr_xor |= (1 << i)
                    node = node.children[opposite]
                else:
                    node = node.children[bit]
            
            max_xor = max(max_xor, curr_xor)
        
        return max_xor