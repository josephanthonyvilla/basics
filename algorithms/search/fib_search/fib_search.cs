using System;
  
class basics {
    public static int search(int[] arr, int key) {
        int len = arr.Length - 1;
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
        if (fib2 != 0 && arr[offset + 1] == key) {
            return offset + 1;
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
        result(search(arr, -5));
        result(search(arr, 2));
        result(search(arr, 69));
    }
}