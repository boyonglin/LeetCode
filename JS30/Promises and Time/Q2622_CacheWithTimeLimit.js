class TimeLimitedCache {

    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        const found = this.cache.has(key);

        // replace
        if (found) {
            clearTimeout(this.cache.get(key).timerId);
        }

        // set delete timer
        this.cache.set(key, {
            value,
            timerId: setTimeout(() => this.cache.delete(key), duration)
        });

        return found;
    }

    get(key) {
        return this.cache.has(key) ? this.cache.get(key).value : -1;
    }

    count() {
        return this.cache.size; // Map, Set -> size
    }
}

const timeLimitedCache = new TimeLimitedCache()
console.log(timeLimitedCache.set(1, 42, 1000));
console.log(timeLimitedCache.get(1));
console.log(timeLimitedCache.count());