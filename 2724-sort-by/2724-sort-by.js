/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    // We use the built-in sort() method.
    // The comparison function (a, b) => fn(a) - fn(b) 
    // sorts the elements based on the values returned by fn.
    return arr.sort((a, b) => fn(a) - fn(b));
};