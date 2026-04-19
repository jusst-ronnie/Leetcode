class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        max_dist = 0
        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                # Valid pair: calculate distance and try to extend j further
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # Invalid pair: nums1[i] is too large, move i to a smaller value
                i += 1
                
        return max_dist