/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    // 1. Edge case: if obj is null/undefined or classFunction is invalid
    if (obj === null || obj === undefined || typeof classFunction !== 'function') {
        return false;
    }

    // 2. Start looking at the prototype of the current object
    // Object(obj) handles primitives like 5 by "boxing" them into Number(5)
    let currPrototype = Object.getPrototypeOf(Object(obj));

    // 3. Walk up the chain until we find the class or hit null
    while (currPrototype !== null) {
        if (currPrototype === classFunction.prototype) {
            return true;
        }
        currPrototype = Object.getPrototypeOf(currPrototype);
    }

    return false;
};