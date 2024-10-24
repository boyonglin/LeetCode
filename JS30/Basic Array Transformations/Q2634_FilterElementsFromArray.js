var filter = function(arr, fn) {
    const res = [];

    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            res.push(arr[i]);
        }
    }

    return res;
};

let fn = function greaterThan10(n) { return n > 10; }
let arr = [0, 10, 20, 30];
console.log(filter(arr, fn));