using System;

class QuickSort
{
    static void Main()
    {
        int[] arr = { 3, 6, 8, 10, 1, 2, 1 };
        QuickSortArray(arr, 0, arr.Length - 1);

        foreach (int num in arr)
        {
            Console.Write(num + " ");
        }
    }

    static void QuickSortArray(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int pivotIndex = Partition(arr, low, high);
            QuickSortArray(arr, low, pivotIndex - 1);
            QuickSortArray(arr, pivotIndex + 1, high);
        }
    }

    static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp2 = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp2;

        return i + 1;
    }
}
