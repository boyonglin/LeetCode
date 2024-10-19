function memoize(fn) {
    const cache = {};

    return function(...args) {
        const key = JSON.stringify(args);

        // if (!(key in cache)) { ... }
        if (typeof(cache[key]) === "undefined") {
            cache[key] = fn(...args);
        }
        return cache[key];
    }
}

let callCount = 0;
const memoizedFn = memoize(function (a, b) {
    callCount += 1;
    return a + b;
})

console.log(memoizedFn(2, 3))
console.log(memoizedFn(2, 3))
console.log(callCount)
console.log(memoizedFn(1, 2))
console.log(callCount)