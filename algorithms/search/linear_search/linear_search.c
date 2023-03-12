#include <stdio.h>

int search(int arr[], int len, int key) {
    for(int i = 0; i < len; i++){
        if(arr[i] == key) return i;
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
    int arr[] = {0, 42, 69, 17, -5, 2, 9, 1};
    int len = sizeof(arr) / sizeof(arr[0]);

    result(search(arr, len, 3));
    result(search(arr, len, 2));

    return 0;
}