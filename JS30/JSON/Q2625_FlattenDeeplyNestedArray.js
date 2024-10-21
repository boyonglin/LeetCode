var flat = function (arr, n) {
    const res = [];

    for (let val of arr) {
        if (Array.isArray(val) && n > 0) {
            res.push(...flat(val, n - 1));
        } else {
            res.push(val);
        }
    }
    
    return res;
};

const arr = [1,2,3,[4,5,6],[7,8,[9,10,11],12],[13,14,15]];
const n = 1;
console.log(flat(arr, n));