var minimumDistance = function(nums) {
    const positions = new Map();
    
    // Store indices for each number
    for (let i = 0; i < nums.length; i++) {
        if (!positions.has(nums[i])) {
            positions.set(nums[i], []);
        }
        positions.get(nums[i]).push(i);
    }
    
    let ans = Infinity;
    
    // Check each number
    for (let indices of positions.values()) {
        if (indices.length >= 3) {
            for (let i = 0; i < indices.length - 2; i++) {
                let first = indices[i];
                let last = indices[i + 2];
                
                let dist = 2 * (last - first);
                ans = Math.min(ans, dist);
            }
        }
    }
    
    return ans === Infinity ? -1 : ans;
};