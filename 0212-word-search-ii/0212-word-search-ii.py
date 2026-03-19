class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store full word


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        
        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        
        m, n = len(board), len(board[0])
        result = []

        def dfs(i, j, node):
            ch = board[i][j]
            
            if ch not in node.children:
                return
            
            nextNode = node.children[ch]
            
            # Found a word
            if nextNode.word:
                result.append(nextNode.word)
                nextNode.word = None   # avoid duplicates
            
            # Mark visited
            board[i][j] = '#'
            
            # Explore neighbors
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, nextNode)
            
            # Backtrack
            board[i][j] = ch
            
            # 🔥 Optimization: remove leaf node
            if not nextNode.children:
                node.children.pop(ch)

        # Start DFS
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return result