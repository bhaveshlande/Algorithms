using System;

class BubbleSort {
    public static void Sort(int[] arr) {
        /**
         * Sorts an array using the Bubble Sort algorithm.
         *
         * @param arr The input array to be sorted.
         */
        int n = arr.Length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void Main(string[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        Sort(arr);
        foreach (int num in arr) {
            Console.Write(num + " ");
        }
    }
}
