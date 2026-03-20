class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # Result dimensions: (m - k + 1) x (n - k + 1)
        res_rows = m - k + 1
        res_cols = n - k + 1
        ans = [[0] * res_cols for _ in range(res_rows)]
        
        for i in range(res_rows):
            for j in range(res_cols):
                # 1. Extract distinct elements in the current k x k window
                distinct_elements = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        distinct_elements.add(grid[r][c])
                
                # 2. Convert to sorted list to find the smallest gap
                nums = sorted(list(distinct_elements))
                
                # If only one unique element exists, the difference is 0
                if len(nums) < 2:
                    ans[i][j] = 0
                    continue
                
                # 3. Find the minimum difference between adjacent sorted numbers
                min_diff = float('inf')
                for idx in range(len(nums) - 1):
                    diff = nums[idx+1] - nums[idx]
                    if diff < min_diff:
                        min_diff = diff
                
                ans[i][j] = min_diff
                
        return ans