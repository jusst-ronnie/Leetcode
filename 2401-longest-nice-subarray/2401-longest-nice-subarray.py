class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        left = 0
        current_mask = 0
        max_length = 0
        
        for right in range(len(nums)):
            
            # Remove elements until no conflict
            while (current_mask & nums[right]) != 0:
                current_mask ^= nums[left]
                left += 1
            
            # Add current number
            current_mask |= nums[right]
            
            max_length = max(max_length, right - left + 1)
        
        return max_length