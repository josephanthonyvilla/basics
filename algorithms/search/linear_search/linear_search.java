class linear_search {
    public static int search(int arr[], int key ) {
        for( int i=0; i < arr.length; i++) {
            if(arr[i]==key) {
                return i;
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
        int arr[] = {0, 42, 69, 17, -5, 2, 9, 1};
        result(search(arr, 3));
        result(search(arr, 2));
    }
}