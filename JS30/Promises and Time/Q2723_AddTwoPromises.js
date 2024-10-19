var addTwoPromises = async function(promise1, promise2) {

    // const [res1, res2] = await Promise.all([promise1, promise2]);

    return Promise.all([promise1, promise2]).then(([res1, res2]) => {
        return res1 + res2;
    });
};

addTwoPromises(Promise.resolve(2), Promise.resolve(2)).then(console.log);