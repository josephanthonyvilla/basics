function search(arr, low, high, key) {
    let idx;

    if (low <= high && key >= arr[low] && key <= arr[high]) {

        idx = low 
            + Math.floor(((high - low) / (arr[high] - arr[low])) 
            * (key - arr[low]));;

        if (arr[idx] == key)
            return idx;

        if (arr[idx] < key)
            return search(arr, idx + 1, high, key);

        if (arr[idx] > key)
            return search(arr, low, idx - 1, key);
    }
    return -1;
}

function result(idx) {
    (idx === -1)
        ? console.log("Element not found")
        : console.log("Element found at index " + idx);
}

let arr = [11, 12, 14, 17, 19, 20, 21, 22, 25, 34, 36, 42, 47];
let n = arr.length - 1;
result(search(arr, 0, n, 23));
result(search(arr, 0, n, 11));
result(search(arr, 0, n, 22));
result(search(arr, 0, n, 47));