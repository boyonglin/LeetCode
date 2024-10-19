var timeLimit = function (fn, t) {

    return async function (...args) {

        const timeoutPromise = new Promise((resolve, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);

            fn(...args)
                .then(resolve)
                .catch(reject)
        })

        return timeoutPromise;

        // const fnPromise = fn(...args);
        // return Promise.race([fnPromise, timeoutPromise]);
    }
};

fn = async (n) => {
    await new Promise(res => setTimeout(res, 100));
    return n * n;
}
inputs = [5]
t = 50

const limited = timeLimit(fn, t);
limited(...inputs).then(console.log).catch(console.log);