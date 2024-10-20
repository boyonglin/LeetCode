var promiseAll = function(promises) {
    const res = [];
    let resolveCounter = 0;

    return new Promise((resolve, reject) => {
        promises.forEach((promise, index) => {
            promise()
                .then((value) => {
                    res[index] = value;
                    resolveCounter += 1;

                    if (resolveCounter === promises.length) {
                        resolve(res);
                    }
                })
                .catch(reject);
        });
    });
};

promises = [
    () => new Promise(resolve => setTimeout(() => resolve(4), 50)),
    () => new Promise(resolve => setTimeout(() => resolve(10), 150)),
    () => new Promise(resolve => setTimeout(() => resolve(16), 100))
]

promiseAll(promises).then(console.log);