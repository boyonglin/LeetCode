var createCounter = function(init) {
    let counter = init;
    return {
        increment: () => counter += 1,
        decrement: () => counter -= 1,
        reset: () => (counter = init)
    }
};

const counter = createCounter(5)
console.log(counter.increment());
console.log(counter.reset());
console.log(counter.decrement());