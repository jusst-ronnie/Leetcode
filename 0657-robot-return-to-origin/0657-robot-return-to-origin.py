class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # We only need to check if U == D and L == R
        # No need to actually simulate a 2D grid
        return moves.count('U') == moves.count('D') and \
               moves.count('L') == moves.count('R')
