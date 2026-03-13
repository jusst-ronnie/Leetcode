/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    // 1. Check if the array is empty
    if (this.length === 0) {
        return -1;
    }
    
    // 2. Return the element at the last index (length - 1)
    return this[this.length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */