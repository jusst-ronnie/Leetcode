/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    // 1. Base case: If it's not an object or it's null, return as is
    if (obj === null || typeof obj !== 'object') {
        return obj;
    }

    // 2. Handle Arrays
    if (Array.isArray(obj)) {
        return obj
            .filter(Boolean) // Remove falsy values first
            .map(compactObject); // Recursively compact nested elements
    }

    // 3. Handle Objects
    const compacted = {};
    for (const key in obj) {
        const value = compactObject(obj[key]); // Recurse first
        if (Boolean(value)) { // Only add if the resulting value is truthy
            compacted[key] = value;
        }
    }
    
    return compacted;
};