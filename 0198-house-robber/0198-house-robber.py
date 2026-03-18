class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2, prev1 = 0, 0
        
        for amount in nums:
            # Calculate max for current house
            # current = max(skip current house, rob current house)
            current = max(prev1, amount + prev2)
            
            # Update variables for the next iteration
            prev2 = prev1
            prev1 = current
            
        return prev1