/**
 * @param {number[]} nums
 * @return {number}
 */
var beautifulSplits = function(nums) {
    const n = nums.length;
    let count = 0;

    // 1. Precompute LCP table: O(n^2)
    // lcp[i][j] = longest common prefix starting at nums[i] and nums[j]
    const lcp = Array.from({ length: n + 1 }, () => new Int32Array(n + 1).fill(0));
    
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (nums[i] === nums[j]) {
                lcp[i][j] = 1 + lcp[i + 1][j + 1];
            }
        }
    }

    // 2. Iterate through split points i and j: O(n^2)
    // nums1: [0, i-1], nums2: [i, j-1], nums3: [j, n-1]
    for (let i = 1; i <= n - 2; i++) {
        for (let j = i + 1; j <= n - 1; j++) {
            const len1 = i;
            const len2 = j - i;
            const len3 = n - j;

            let isBeautiful = false;

            // Condition A: nums1 is a prefix of nums2
            if (len1 <= len2 && lcp[0][i] >= len1) {
                isBeautiful = true;
            } 
            // Condition B: nums2 is a prefix of nums3
            else if (len2 <= len3 && lcp[i][j] >= len2) {
                isBeautiful = true;
            }

            if (isBeautiful) count++;
        }
    }

    return count;
};
