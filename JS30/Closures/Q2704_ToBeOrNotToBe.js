var expect = function(val) {
    
    return {
        toBe: (value) => {
            if (value !== val) {
                throw new Error("Not Equal");
            } else {
                return true;
            }
        },
        notToBe: (value) => {
            if (value === val) {
               throw new Error("Equal");
            } else {
                return true;
            }
        }
    }
};

console.log(expect(5).toBe(5));
console.log(expect(5).notToBe(5));