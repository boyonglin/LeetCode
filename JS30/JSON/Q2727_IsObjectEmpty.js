var isEmpty = function(obj) {
    return Object.keys(obj).length === 0;
};

const obj = {"x": 5, "y": 42}
console.log(isEmpty(obj));