using System;
  
class basics {
    public static int search(int[] arr, int key) {
        int start = 0;
        int end = arr.Length - 1;
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
        if (idx == -1)
            Console.WriteLine("Element not found");
        else
            Console.WriteLine("Element found at index " + idx);
    }
  
    public static void Main() {
        int[] arr = {-5, 0, 1, 2, 9, 17, 42, 69};
        result(search(arr, 3));
        result(search(arr, 2));
    }
}