/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    
    return function(...args) {
        // Create a unique key for the current arguments
        // JSON.stringify is a safe way to turn [2, 2] into " [2,2] "
        const key = JSON.stringify(args);
        
        // Check if we've already calculated this
        if (cache.has(key)) {
            return cache.get(key);
        }
        
        // If not, call the function and store the result
        const result = fn(...args);
        cache.set(key, result);
        
        return result;
    }
}

/** * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 * return a + b;
 * })
 * memoizedFn(2, 2) // 4
 * memoizedFn(2, 2) // 4
 * console.log(callCount) // 1 
 */