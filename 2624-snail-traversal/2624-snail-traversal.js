/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    // 1. Validation check: Does the total capacity match the array length?
    if (rowsCount * colsCount !== this.length) {
        return [];
    }

    // 2. Initialize the result matrix with empty rows
    const result = Array.from({ length: rowsCount }, () => []);

    // 3. Traverse the original array
    for (let i = 0; i < this.length; i++) {
        // Find which column we are currently in
        const col = Math.floor(i / rowsCount);
        
        // Find the row index. 
        // If col is even: move top to bottom (0, 1, 2...)
        // If col is odd: move bottom to top (...2, 1, 0)
        let row;
        if (col % 2 === 0) {
            row = i % rowsCount;
        } else {
            row = (rowsCount - 1) - (i % rowsCount);
        }

        result[row][col] = this[i];
    }

    return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */