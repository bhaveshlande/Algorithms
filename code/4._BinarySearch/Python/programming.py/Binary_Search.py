def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(my_list, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found")
