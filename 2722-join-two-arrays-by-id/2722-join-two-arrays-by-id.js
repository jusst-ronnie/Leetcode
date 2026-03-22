/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const result = {};

    // Step 1: Add all items from arr1 to the map
    for (const item of arr1) {
        result[item.id] = item;
    }

    // Step 2: Merge items from arr2
    for (const item of arr2) {
        if (result[item.id]) {
            // Merge properties, arr2 overrides arr1
            result[item.id] = { ...result[item.id], ...item };
        } else {
            // New id found in arr2
            result[item.id] = item;
        }
    }

    // Step 3: Extract values, sort by ID, and return
    return Object.values(result).sort((a, b) => a.id - b.id);
};