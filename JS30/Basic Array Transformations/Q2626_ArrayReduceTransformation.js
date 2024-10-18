var reduce = function(nums, fn, init) {
    let res = init;

    for (let i = 0; i < nums.length; i++) {
        res = fn(res, nums[i]);
    }

    return res;
};

nums = [1,2,3,4];
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100;
console.log(reduce(nums, fn, init));