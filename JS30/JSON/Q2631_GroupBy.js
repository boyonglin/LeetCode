Array.prototype.groupBy = function (fn) {
    const grouped = {};

    this.forEach((item) => {
        const key = fn(item);

        if (!grouped[key]) {
            grouped[key] = [];
        }

        grouped[key].push(item);
    })

    return grouped;
};

const array = [
    { "id": "1" },
    { "id": "1" },
    { "id": "2" }
]

const fn = function (item) {
    return item.id;
}

console.log(array.groupBy(fn));