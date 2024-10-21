// ExplainThis

class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, []);  // unsubscribed event
        }

        const events = this.events.get(eventName);
        events.push(callback);  // add callback

        return {
            unsubscribe: () => {
                const index = events.indexOf(callback);
                if (index !== -1) {
                    events.splice(index, 1);  // remove callback
                }
            },
        };
    }

    emit(eventName, args = []) {
        if (!this.events.has(eventName)) {
            return [];  // not being subscribed
        }

        const result = [];
        const events = this.events.get(eventName);

        events.forEach((callback) => {
            result.push(callback(...args));  // call callback
        });

        return result;
    }
}

const emitter = new EventEmitter();

// Subscribe to the onClick event with onClickCallback
function onClickCallback() { return 99 }
const sub = emitter.subscribe('onClick', onClickCallback);

console.log(emitter.emit('onClick'));
console.log(sub.unsubscribe());
console.log(emitter.emit('onClick'));