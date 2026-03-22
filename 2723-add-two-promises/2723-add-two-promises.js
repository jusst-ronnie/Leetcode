/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // Promise.all returns an array of the resolved values [val1, val2]
    const [val1, val2] = await Promise.all([promise1, promise2]);
    
    return val1 + val2;
};