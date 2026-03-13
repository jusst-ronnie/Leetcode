/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timerId;

    return function(...args) {
        // 1. Clear the existing timer if there is one
        // This is the "cancellation" part
        clearTimeout(timerId);

        // 2. Set a new timer
        timerId = setTimeout(() => {
            // 3. Execute the function with the original arguments
            fn(...args);
        }, t);
    };
};