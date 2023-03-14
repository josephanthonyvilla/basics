def search(arr, key):
    n = len(arr) - 1
    offset = -1 # index where value must be to the right
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2
    
    # find first fib larger or equal to n
    while (fib3 < n) :
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
    

    while (fib3 > 1) :
        # make sure idx is a valid location
        idx = min(offset + fib1 , n - 1)

        # value must be from offset to idx
        if (arr[idx] < key) :
            offset = idx
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
        
        # remove subarray after idx
        elif (arr[idx] > key) :
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2
         
        else :
            return idx
        
    
    # compare last elem with key
    if (fib2 != 0 and arr[offset + 1] == key) :
        return offset + 1
    
    return -1

def result(idx):
    if idx == -1:
        print("Element not found")
    else:
        print("Element found at index", idx)

if __name__ == "__main__":
    arr = [-5, 0, 1, 2, 9, 17, 42, 69]
    result(search(arr, 3))
    result(search(arr, -5))
    result(search(arr, 2))
    result(search(arr, 69))