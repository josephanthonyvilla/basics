#include <iostream>
using namespace std;

int search(int arr[], int len, int key) {
    int start = 0;
    int end = len - 1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
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
    result(search(arr, len, 2));

    return 0;
}