function sortBy(arr, fn) {
    return arr.toSorted((a, b) => fn(a) - fn(b));  // compare function
};

const arr = [{"x": 1}, {"x": 0}, {"x": -1}], fn = (d) => d.x;
console.log(sortBy(arr, fn));

// compare function return value
// > 0: b comes first
// < 0: a comes first
// = 0: no change