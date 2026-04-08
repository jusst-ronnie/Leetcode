/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var xorAfterQueries = function(nums, queries) {
    const MOD = 1000000007;
    const n = nums.length;

    for (const [l, r, k, v] of queries) {
        for (let i = l; i <= r; i += k) {
            // Use BigInt for multiplication to prevent overflow before modulo
            nums[i] = Number((BigInt(nums[i]) * BigInt(v)) % BigInt(MOD));
        }
    }

    let xorSum = 0;
    for (const num of nums) {
        xorSum ^= num;
    }

    return xorSum;
};