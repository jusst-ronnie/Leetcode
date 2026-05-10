class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Initialize dp array with -1 (unreachable)
        dp = [-1] * n
        # Base case: 0 jumps to reach the first index
        dp[0] = 0
        
        for i in range(n):
            # Only proceed if the current index i is reachable
            if dp[i] == -1:
                continue
                
            for j in range(i + 1, n):
                # Check the target condition
                if abs(nums[j] - nums[i]) <= target:
                    # Update dp[j] with the maximum jumps found so far
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return dp[n - 1]