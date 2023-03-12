def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def result(idx):
    if idx == -1:
        print("Element not found")
    else:
        print("Element found at index", idx)

if __name__ == "__main__":
    arr = [0, 42, 69, 17, -5, 2, 9, 1]
    result(search(arr, 3))
    result(search(arr, 2))