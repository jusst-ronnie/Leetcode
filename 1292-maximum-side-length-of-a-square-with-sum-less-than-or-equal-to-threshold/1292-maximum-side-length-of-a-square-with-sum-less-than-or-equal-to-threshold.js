/**
 * @param {number[][]} mat
 * @param {number} threshold
 * @return {number}
 */
var maxSideLength = function(mat, threshold) {
    const m = mat.length;
    const n = mat[0].length;
    
    // 1. Build 2D Prefix Sum table
    // prefix[i][j] is the sum of mat[0...i-1][0...j-1]
    const prefix = Array.from({ length: m + 1 }, () => new Float64Array(n + 1));
    
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            prefix[i][j] = mat[i-1][j-1] 
                         + prefix[i-1][j] 
                         + prefix[i][j-1] 
                         - prefix[i-1][j-1];
        }
    }
    
    let maxSide = 0;
    
    // 2. Iterate and expand the side length greedily
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            // Check if we can form a square of size (maxSide + 1)
            // ending at the current (i, j)
            let k = maxSide + 1;
            
            if (i >= k && j >= k) {
                let currentSum = prefix[i][j] 
                               - prefix[i-k][j] 
                               - prefix[i][j-k] 
                               + prefix[i-k][j-k];
                
                if (currentSum <= threshold) {
                    maxSide++; // We found a larger valid square!
                }
            }
        }
    }
    
    return maxSide;
};