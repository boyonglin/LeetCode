var cancellable = function(fn, args, t) {
    console.log(fn(...args));

    const intervalId = setInterval(() => {
        console.log(fn(...args));
    }, t);

    return function cancelFn() {
        clearInterval(intervalId);
    };
};

const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);