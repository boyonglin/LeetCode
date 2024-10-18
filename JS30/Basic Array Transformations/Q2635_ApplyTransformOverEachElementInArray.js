var map = function(arr, fn) {
    const res = [];

    for (let i = 0; i < arr.length; i++) {
        res.push(fn(arr[i], i));
    }

    return res;
};

fn = function plusI(n, i) { return n + i; }
arr = [1, 2, 3];
console.log(map(arr, fn));