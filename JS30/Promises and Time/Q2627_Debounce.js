var debounce = function(fn, delay) {
    let inputTimer;

    return function(...args) {
        clearTimeout(inputTimer);

        inputTimer = setTimeout(() => {
            fn(...args);
        }, delay);
    }
};

const debounced = debounce((x) => console.log(x), 50);
setTimeout(() => debounced(1), 50);
setTimeout(() => debounced(2), 75);