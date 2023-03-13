#include <iostream>
using namespace std;

int search(int arr[], int low, int high, int key) {
    int idx;
    if(low <= high && key >= arr[low] && key <= arr[high]) {

        idx = low + (((double)(high - low) / (arr[high] - arr[low])) * (key - arr[low]));
        
        if(arr[idx] == key) {
            return idx;
        }

        // key is in left sub array
        if(arr[idx] > key) {
            return search(arr, low, idx - 1, key);
        }

        // key is in right sub array
        if(arr[idx] < key){
            return search(arr, idx + 1, high, key);
        }    
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
    int arr[] = {11, 12, 14, 17, 19, 20, 21, 22, 25, 34, 36, 42, 47};
    int n = sizeof(arr) / sizeof(arr[0]);

    result(search(arr, 0, n, 23));
    result(search(arr, 0, n, 11));
    result(search(arr, 0, n, 22));
    result(search(arr, 0, n, 47));

    return 0;
}