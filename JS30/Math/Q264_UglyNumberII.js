var nthUglyNumber = function(n) {
    // indices
    let i2 = 0, i3 = 0, i5 = 0;
    let cache = [1];

    while(!cache[n-1]) {
        // candidates
        let c2 = cache[i2] * 2;
        let c3 = cache[i3] * 3;
        let c5 = cache[i5] * 5;

        // maintain the order
        let next = Math.min(Math.min(c2, c3), c5);
        cache.push(next);

        if (next === c2) i2++;
        if (next === c3) i3++;
        if (next === c5) i5++;
    }

    return cache[n-1];
};

let n = 10;
console.log(nthUglyNumber(n));
