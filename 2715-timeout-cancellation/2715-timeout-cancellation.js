/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // 1. Schedule the function execution
    const timerId = setTimeout(() => {
        fn(...args);
    }, t);

    // 2. Return a function that can cancel the scheduled execution
    return function cancelFn() {
        clearTimeout(timerId);
    };
};