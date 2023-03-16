def sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        sort(left)
        sort(right)

        i = j = k = 0

        # copy to temp array
        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # get any leftover elems
        while(i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1

        while(j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    unsorted = [9, 42, 2, 0, 69, -5, 420, 27]
    sorted = [-5, 0, 2, 9, 27, 42, 69, 420]

    if(unsorted != sorted):
        print("PASSED")
    else:
        print("FAILED")
    
    sort(unsorted)

    if(unsorted == sorted):
        print("PASSED")
    else:
        print("FAILED")