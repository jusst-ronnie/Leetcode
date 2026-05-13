class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # delta[i] stores the change in moves needed for target sum i
        # Range is 2 to 2*limit. Use 2*limit + 2 for safety.
        delta = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # 1. Default: Assume 2 moves for all possible sums
            # range [2, 2*limit]
            delta[2] += 2
            delta[2 * limit + 1] -= 2
            
            # 2. To take only 1 move:
            # Range: [min(a, b) + 1, max(a, b) + limit]
            # We subtract 1 move from the default 2 moves
            low = min(a, b) + 1
            high = max(a, b) + limit
            delta[low] -= 1
            delta[high + 1] += 1
            
            # 3. To take 0 moves:
            # Only when S == a + b
            # We subtract another 1 move from the 1 move calculated above
            sum_ab = a + b
            delta[sum_ab] -= 1
            delta[sum_ab + 1] += 1
            
        # Sweep line to find the minimum moves
        min_moves = n
        current_moves = 0
        for i in range(2, 2 * limit + 1):
            current_moves += delta[i]
            if current_moves < min_moves:
                min_moves = current_moves
                
        return min_moves