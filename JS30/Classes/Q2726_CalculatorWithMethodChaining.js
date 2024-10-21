class Calculator {

    constructor(value) {
        this.res = value ;
    }

    add(value){
        this.res += value;
        return this;
    }

    subtract(value){
        this.res -= value;
        return this;
    }

    multiply(value) {
        this.res *= value;
        return this;
    }

    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        } else {
            this.res /= value;
            return this;
        }
    }

    power(value) {
        this.res = Math.pow(this.res, value);
        return this;  // return object -> enable chaining
    }

    getResult() {
        return this.res;  // return result
    }
}

const calc = new Calculator(2);
console.log(calc.multiply(5).power(2).getResult());