#include <iostream>
#include <vector>

int binarySearch(const std::vector<int> &arr, int target)
{
    int left = 0, right = arr.size() - 1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    return -1; // Target not found
}

int main()
{
    std::vector<int> arr = {1, 3, 5, 7, 9, 11, 13};
    int target = 7;
    int result = binarySearch(arr, target);
    if (result != -1)
    {
        std::cout << "Target " << target << " found at index " << result << std::endl;
    }
    else
    {
        std::cout << "Target not found" << std::endl;
    }
    return 0;
}
