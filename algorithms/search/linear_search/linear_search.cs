using System;
  
class basics {
    public static int search(int[] arr, int key) {
        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] == key)
                return i;
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
        int[] arr = {0, 42, 69, 17, -5, 2, 9, 1};

        result(search(arr, 3));
        result(search(arr, 2));
    }
}