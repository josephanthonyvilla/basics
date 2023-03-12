class binary_search {
    public static int search(int arr[], int key ) {
        int start = 0;
        int end = arr.length - 1;
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

    public static void result(int idx) {
        if (idx == -1) {
            System.out.print("Element not found \n");
        } else {
            System.out.print("Element found at index " + idx + " \n");
        }
    }

    public static void main(String[] args) {
        int arr[] = {-5, 0, 1, 2, 9, 17, 42, 69};
        result(search(arr, 3));
        result(search(arr, 2));
    }
}