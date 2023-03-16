class merge_sort {
    void merge(int arr[], int l, int m, int r) {
        int i, j, k;
        int len1 = m - l + 1;
        int len2 = r - m;
    
        int left[] = new int[len1];
        int right[] = new int[len2];
    
        // copy to temporary sub arrays
        for (i = 0; i < len1; i++)
            left[i] = arr[l + i];
        for (j = 0; j < len2; j++)
            right[j] = arr[m + 1 + j];
    
        // index of first, second, and merged subarrays
        i = 0;
        j = 0;
        k = l;
    
        // merge temp arrays back
        while (i < len1 && j < len2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
        // copy remaining elements of left subarray
        while (i < len1) {
            arr[k] = left[i];
            i++;
            k++;
        }
        // copy remaining elements of right subarray
        while (j < len2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }
    
    void sort(int arr[], int l, int r){
        if (l < r) {
            int m = (l + r) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
    
    static void result(int unsorted[], int sorted[], int len, int expected){
        int match = 1;
        for (int i = 0; i < len; i++){
            if(unsorted[i] != sorted[i]){
                match = 0;
                break;
            }
        }
        if(match != expected){
            System.out.println("FAILED");
        } else {
            System.out.println("PASSED");   
        }
    } 

    public static void main(String[] args) {
        int unsorted[] = {9, 42, 2, 0, 69, -5, 420, 27};
        int sorted[] = {-5, 0, 2, 9, 27, 42, 69, 420};
        int len = unsorted.length;

        result(unsorted, sorted, len, 0);
        merge_sort ob = new merge_sort();
        ob.sort(unsorted, 0, len - 1);
        result(unsorted, sorted, len, 1);
    }
}