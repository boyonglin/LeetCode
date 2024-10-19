var argumentsLength = function(...args) {

    return args.length;

    // for (const index in args) { ... }
};

console.log(argumentsLength(1, 2, 3));