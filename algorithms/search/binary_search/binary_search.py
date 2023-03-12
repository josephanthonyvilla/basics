def search(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
  
    return -1

def result(idx):
    if idx == -1:
        print("Element not found")
    else:
        print("Element found at index", idx)

if __name__ == "__main__":
    arr = [-5, 0, 1, 2, 9, 17, 42, 69]
    result(search(arr, 3))
    result(search(arr, 2))