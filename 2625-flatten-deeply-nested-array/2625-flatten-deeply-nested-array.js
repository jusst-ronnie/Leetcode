/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    // If depth n is 0, no flattening occurs, just return the array
    if (n === 0) return arr;

    const result = [];

    // Helper function to handle recursion
    const flatten = (currentArray, currentDepth) => {
        for (const item of currentArray) {
            // Check if item is an array AND we haven't exceeded depth n
            if (Array.isArray(item) && currentDepth < n) {
                // Recursively call for the subarray, incrementing the depth
                flatten(item, currentDepth + 1);
            } else {
                // Otherwise, push the item (whether it's a number or an unflattened array)
                result.push(item);
            }
        }
    };

    flatten(arr, 0);
    return result;
};