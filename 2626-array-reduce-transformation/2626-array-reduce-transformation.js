/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    // Start with the initial value
    let val = init;
    
    // Iterate through each number in the array
    for (let i = 0; i < nums.length; i++) {
        // Update val by calling fn with the current val and the next element
        val = fn(val, nums[i]);
    }
    
    return val;
};