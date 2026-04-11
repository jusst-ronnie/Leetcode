/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDistance = function(nums) {
    const posMap = new Map();
    
    // Group indices by their value
    for (let i = 0; i < nums.length; i++) {
        if (!posMap.has(nums[i])) {
            posMap.set(nums[i], []);
        }
        posMap.get(nums[i]).push(i);
    }
    
    let minDist = Infinity;
    
    // Iterate through the grouped indices
    for (let indices of posMap.values()) {
        // We need at least 3 occurrences
        if (indices.length < 3) continue;
        
        // Sliding window of size 3
        for (let i = 0; i <= indices.length - 3; i++) {
            // Distance = 2 * (index[i+2] - index[i])
            let currentDist = 2 * (indices[i + 2] - indices[i]);
            if (currentDist < minDist) {
                minDist = currentDist;
            }
        }
    }
    
    return minDist === Infinity ? -1 : minDist;
};