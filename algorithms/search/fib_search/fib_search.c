#include <stdio.h>

int search(int arr[], int len, int key) {
    int offset = -1; // index where value must be to the right
    int fib1 = 0;
    int fib2 = 1;
    int fib3 = fib1 + fib2;
 
    // find first fib larger or equal to len
    while (fib3 < len) {
        fib1 = fib2;
        fib2 = fib3;
        fib3 = fib1 + fib2;
    }
 
    while (fib3 > 1) {
        // make sure idx is a valid location
        int idx = ((offset + fib1) <= (len - 1)) ? (offset + fib1) : (len - 1);

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

int result(int idx) {
    (idx == -1)
       ? printf("Element not found \n")
       : printf("Element found at index %d \n", idx);
    return 0;
} 

int main(void) {
    int arr[] = {-5, 0, 1, 2, 9, 17, 42, 69};
    int len = sizeof(arr) / sizeof(arr[0]);

    result(search(arr, len, 3));
    result(search(arr, len, -5));
    result(search(arr, len, 2));
    result(search(arr, len, 69));

    return 0;
}