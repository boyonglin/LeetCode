var createCounter = function(n) {
    let counts = n - 1;

    return function() {
        return counts += 1
    }
}

const counter = createCounter(10)
console.log(counter())
console.log(counter())
console.log(counter())