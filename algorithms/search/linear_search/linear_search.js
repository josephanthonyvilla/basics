function search(arr, key) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === key) {
            return i;
        }
    }
    return -1;
}

function result(idx) {
    (idx === -1)
        ? console.log("Element not found")
        : console.log("Element found at index " + idx);
}

let arr = [0, 42, 69, 17, -5, 2, 9, 1];
result(search(arr, 3));
result(search(arr, 2));