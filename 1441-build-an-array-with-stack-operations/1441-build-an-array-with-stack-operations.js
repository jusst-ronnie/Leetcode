/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
    const operations = [];
    let targetIndex = 0;
    
    // We iterate through the stream from 1 up to n
    for (let currentStreamNum = 1; currentStreamNum <= n; currentStreamNum++) {
        // If we've already matched all elements in target, stop.
        if (targetIndex >= target.length) break;
        
        if (currentStreamNum === target[targetIndex]) {
            // Match found: just Push.
            operations.push("Push");
            targetIndex++;
        } else {
            // No match: we must Push then Pop to discard the stream number.
            operations.push("Push");
            operations.push("Pop");
        }
    }
    
    return operations;
};