def search(arr, low, high, key):
    if(arr[high] == arr[low]):
        return high
    if(low <= high and key >= arr[low] and key <= arr[high]):
        idx = low + (((high - low) // (arr[high] - arr[low])) * (key - arr[low]))
        if(arr[idx] == key):
            return idx
        if(arr[idx] > key):
            return search(arr, low, idx - 1, key)
        if(arr[idx] < key):
            return search(arr, idx + 1, high, key)
    return -1

def result(idx):
    if idx == -1:
        print("Element not found")
    else:
        print("Element found at index", idx)

if __name__ == "__main__":
    arr = [11, 12, 14, 17, 19, 20, 21, 22, 25, 34, 36, 42, 47]
    n = len(arr) - 1
    result(search(arr, 0, n, 23))
    result(search(arr, 0, n, 11))
    result(search(arr, 0, n, 22))
    result(search(arr, 0, n, 47))
