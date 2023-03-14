function search(arr, key) {
    let len = arr.length - 1;
    let offset = -1; // index where value must be to the right
    let fib1 = 0;
    let fib2 = 1;
    let fib3 = fib1 + fib2;

    // find first fib larger or equal to len
    while (fib3 < len) {
        fib1 = fib2;
        fib2 = fib3;
        fib3 = fib1 + fib2;
    }

    while (fib3 > 1) {
        // make sure idx is a valid location
        let idx = Math.min((offset + fib1) , (len - 1));

        // value must be from offset to idx
        if (arr[idx] < key) {
            offset = idx;
            fib3 = fib2;
            fib2 = fib1;
            fib1 = fib3 - fib2;
        }
        // remove subarray after idx
        else if (arr[idx] > key) {
            fib3 = fib1;
            fib2 = fib2 - fib1;
            fib1 = fib3 - fib2;
        } 
        else {
            return idx;
        }
    }
    // compare last elem with key
    if (fib2 && arr[offset + 1] == key) {
        return offset + 1;
    }
    return -1;
}

function result(idx) {
    (idx === -1)
        ? console.log("Element not found")
        : console.log("Element found at index " + idx);
}

let arr = [-5, 0, 1, 2, 9, 17, 42, 69];
result(search(arr, 3));
result(search(arr, -5));
result(search(arr, 2));
result(search(arr, 69));
