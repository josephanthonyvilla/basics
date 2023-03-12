function search(arr, key) {
    let start = 0;
    let end = arr.length - 1;
    while (start <= end) {
        let mid = start + Math.floor((end - start) / 2);
        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] < key) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
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
result(search(arr, 2));