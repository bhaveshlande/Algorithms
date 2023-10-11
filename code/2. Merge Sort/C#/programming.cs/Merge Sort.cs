using System;

class MergeSort
{
    static void Main()
    {
        int[] arr = { 3, 6, 8, 10, 1, 2, 1 };
        MergeSortArray(arr);

        foreach (int num in arr)
        {
            Console.Write(num + " ");
        }
    }

    static void MergeSortArray(int[] arr)
    {
        int n = arr.Length;
        if (n < 2)
            return;

        int mid = n / 2;
        int[] left = new int[mid];
        int[] right = new int[n - mid];

        for (int i = 0; i < mid; i++)
        {
            left[i] = arr[i];
        }
        for (int i = mid; i < n; i++)
        {
            right[i - mid] = arr[i];
        }

        MergeSortArray(left);
        MergeSortArray(right);

        Merge(arr, left, right);
    }

    static void Merge(int[] arr, int[] left, int[] right)
    {
        int leftLength = left.Length;
        int rightLength = right.Length;
        int i = 0, j = 0, k = 0;

        while (i < leftLength && j < rightLength)
        {
            if (left[i] <= right[j])
            {
                arr[k] = left[i];
                i++;
            }
            else
            {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < leftLength)
        {
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < rightLength)
        {
            arr[k] = right[j];
            j++;
            k++;
        }
    }
}
