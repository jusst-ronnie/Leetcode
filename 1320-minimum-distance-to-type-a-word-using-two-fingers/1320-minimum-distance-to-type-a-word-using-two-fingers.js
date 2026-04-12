/**
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    const memo = new Map();

    const getDist = (char1, char2) => {
        if (char1 === null) return 0;
        
        const p1 = char1.charCodeAt(0) - 65;
        const p2 = char2.charCodeAt(0) - 65;
        
        const r1 = Math.floor(p1 / 6), c1 = p1 % 6;
        const r2 = Math.floor(p2 / 6), c2 = p2 % 6;
        
        return Math.abs(r1 - r2) + Math.abs(c1 - c2);
    };

    const solve = (idx, f1, f2) => {
        if (idx === word.length) return 0;

        // Create a unique key for the memoization map
        const state = `${idx},${f1},${f2}`;
        if (memo.has(state)) return memo.get(state);

        const target = word[idx];

        // Choice 1: Move Finger 1
        const moveF1 = getDist(f1, target) + solve(idx + 1, target, f2);

        // Choice 2: Move Finger 2
        const moveF2 = getDist(f2, target) + solve(idx + 1, f1, target);

        const res = Math.min(moveF1, moveF2);
        memo.set(state, res);
        return res;
    };

    return solve(0, null, null);
};
