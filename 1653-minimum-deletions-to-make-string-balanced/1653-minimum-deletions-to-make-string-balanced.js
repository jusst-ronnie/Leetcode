/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    let deletions = 0;
    let bCount = 0;
    
    for (let char of s) {
        if (char === 'b') {
            // Found a 'b', just increment our 'b' counter
            bCount++;
        } else {
            // Found an 'a'
            // We decide: is it cheaper to delete this 'a' OR 
            // delete all the 'b's we've seen so far?
            deletions = Math.min(deletions + 1, bCount);
        }
    }
    
    return deletions;
};