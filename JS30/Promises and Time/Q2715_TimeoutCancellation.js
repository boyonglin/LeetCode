var cancellable = function(fn, args, t) {

    // excute the function after t ms
    const timerId = setTimeout(() => {
        console.log(fn(...args));
    }, t);

    // cancel the execution after cancelTimeMs ms
    return function cancelFn() {
        clearTimeout(timerId);
    };
};

const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x**2, [2], 20);
setTimeout(cancelFn, cancelTimeMs);