class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # 1. Determine n (the maximum value)
        n = len(nums) - 1
        
        # Base case: The array must have at least 2 elements [1, 1]
        if n < 1:
            return False
            
        # 2. Sort the array to easily check the sequence
        nums.sort()
        
        # 3. Check numbers from index 0 to n-1
        # They should match [1, 2, 3, ..., n]
        for i in range(n):
            if nums[i] != i + 1:
                return False
        
        # 4. Check the last element
        # It must be equal to n (making it the second occurrence of n)
        return nums[n] == n
