Array.prototype.last = function() {
    return this.length > 0 ? this[this.length - 1] : -1;
};

const nums = [null, {}, 3]
console.log(nums.last());