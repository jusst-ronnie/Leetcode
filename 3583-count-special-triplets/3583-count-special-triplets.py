from collections import Counter

class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Count total occurrences of each number to identify "right side" counts
        right_count = Counter(nums)
        left_count = Counter()
        
        total_triplets = 0
        
        for j in range(n):
            # The current element is our pivot (nums[j])
            # It can no longer be on the "right" of any previous pivot
            right_count[nums[j]] -= 1
            
            target = nums[j] * 2
            
            # If target exists in both left and right, add L * R to total
            if target in left_count and target in right_count:
                L = left_count[target]
                R = right_count[target]
                # Modulo at each addition to prevent overflow and keep results within range
                total_triplets = (total_triplets + (L * R)) % MOD
            
            # Now the current element moves to the "left" for future pivots
            left_count[nums[j]] += 1
            
        return total_triplets