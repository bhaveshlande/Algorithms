using System;

class BinarySearch
{
    static int BinarySearchArray(int[] arr, int target)
    {
        int left = 0;
        int right = arr.Length - 1;
        
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target)
                return mid;
            else if (arr[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        
        return -1;  // Target not found
    }

    static void Main()
    {
        int[] arr = { 1, 3, 5, 7, 9, 11, 13 };
        int target = 7;
        int result = BinarySearchArray(arr, target);

        if (result != -1)
            Console.WriteLine($"Target {target} found at index {result}");
        else
            Console.WriteLine("Target not found");
    }
}
