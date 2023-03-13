using System;
  
class basics {
    public static int search(int[] arr, int low, int high, int key) {
        if(arr[high] == arr[low])
            return high;
            
        int idx;
        if (low <= high && key >= arr[low] && key <= arr[high]) {

            idx = low + (((high - low) / (arr[high] - arr[low])) * (key - arr[low]));
 
            if (arr[idx] == key)
                return idx;
 
            if (arr[idx] < key)
                return search(arr, idx + 1, high, key);
 
            if (arr[idx] > key)
                return search(arr, low, idx - 1, key);
        }
        return -1;
    }

    public static void result(int idx) {
        if (idx == -1)
            Console.WriteLine("Element not found");
        else
            Console.WriteLine("Element found at index " + idx);
    }
  
    public static void Main() {
        int[] arr = {11, 12, 14, 17, 19, 20, 21, 22, 25, 34, 36, 42, 47};
        int n = arr.Length - 1;
        result(search(arr, 0, n, 23));
        result(search(arr, 0, n, 11));
        result(search(arr, 0, n, 22));
        result(search(arr, 0, n, 47));
    }
}