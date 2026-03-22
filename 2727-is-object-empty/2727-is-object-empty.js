/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // If it's an array, obj.length will be defined.
    // If it's an object, Object.keys(obj) returns an array of keys.
    // In both cases, we check if the count of elements/keys is 0.
    
    if (Array.isArray(obj)) {
        return obj.length === 0;
    }
    
    return Object.keys(obj).length === 0;
};