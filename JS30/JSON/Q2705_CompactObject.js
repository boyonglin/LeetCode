// ExplainThis

var compactObject = function (obj) {

    if (Array.isArray(obj)) {
        return obj
            .map(compactObject)  // recursive call
            .filter(Boolean);    // false, null, undefined, 0, NaN, "" are removed
    } else if (typeof obj === "object" && obj !== null) {
        const result = {};

        for (let key in obj) {
            const value = compactObject(obj[key]);
            if (Boolean(value)) {
                result[key] = value;
            }
        }
        return result;  // if not object or array (e.g. string, number), return as is
    }

    return obj;
};