/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // 1. Execute immediately at 0ms
    fn(...args);

    // 2. Set up the interval to run every t ms
    const timerId = setInterval(() => {
        fn(...args);
    }, t);

    // 3. Return the cancel function
    const cancelFn = () => {
        clearInterval(timerId);
    };

    return cancelFn;
};