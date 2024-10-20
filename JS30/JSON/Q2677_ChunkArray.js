var chunk = function (arr, size) {
    const res = [];
    let temp = [];

    arr.forEach((value, index) => {
        temp.push(value);

        if (temp.length === size || index === arr.length - 1) {
            res.push(temp);
            temp = [];
        }

        // res.push(arr.slice(i, i + size));
    });

    return res;
};

const arr = [1, 2, 3, 4, 5, 6, 7, 8];
const size = 3;
console.log(chunk(arr, size));