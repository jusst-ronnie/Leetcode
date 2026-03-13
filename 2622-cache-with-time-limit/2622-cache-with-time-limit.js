var TimeLimitedCache = function() {
    this.cache = new Map(); // Stores key -> {value, timeoutId}
};

/** * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exists = this.cache.has(key);
    
    // If it exists, clear the old timer so it doesn't delete the new value early
    if (exists) {
        clearTimeout(this.cache.get(key).timeoutId);
    }
    
    // Set a new timer to delete the key after 'duration'
    const timeoutId = setTimeout(() => {
        this.cache.delete(key);
    }, duration);
    
    this.cache.set(key, { value, timeoutId });
    
    return exists;
};

/** * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.cache.has(key) ? this.cache.get(key).value : -1;
};

/** * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};