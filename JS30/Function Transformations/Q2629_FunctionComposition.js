var compose = function(functions) {

    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x)

        // for (let i = functions.length - 1; i >= 0; i--) { ... }
    }
};

const fn = compose([x => x + 1, x => 2 * x]);
console.log(fn(4));