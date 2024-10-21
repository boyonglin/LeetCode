var throttle = function (fn, delay) {
    let timer = null;

    return (...args) => {
        if (timer) return;

        timer = setTimeout(() => {
            fn(...args);
            timer = null;
        }, delay);
    };
}

const throttled = throttle(() => console.log("throttle"), 100);

// if keep scrolling, the console will keep logging "throttle" every 100ms
// window.addEventListener("scroll", () => {
//     throttled();
// });
