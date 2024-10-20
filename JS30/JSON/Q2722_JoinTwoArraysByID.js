var join = function(arr1, arr2) {
    const joined = {};

    for (const obj of arr1) {
        joined[obj.id] = obj;
    }

    for (const obj of arr2) {
        joined[obj.id] = { ...joined[obj.id], ...obj };  // arr2 will overwrite arr1 -> .assign()
    }

    // const joined = arr1.concat(arr2).reduce((acc, obj) => {
    //     acc[obj.id] = Object.assign(acc[obj.id] || {}, obj);  // if obj.id is not in acc, create a new object
    //     return acc;
    // }, {});  // {} is the initial value of acc

    return Object.values(joined);
};

const arr1 = [{"id":1,"b":{"b": 94},"v":[4,3],"y":48}];
const arr2 = [{"id":1,"b":{"c": 84},"v":[1,3]}];
console.log(join(arr1, arr2));