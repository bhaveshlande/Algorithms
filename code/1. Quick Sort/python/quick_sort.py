# Define a function for quick sort that takes an array 'arr' as input.
def quick_sort(arr):
    # Base case: If the length of the array is 0 or 1, it is already sorted, so return the array as is.
    if len(arr) <= 1:
        return arr

    # Select the pivot element as the middle element of the array.
    pivot = arr[len(arr) // 2]

    # Create three sub-arrays:
    # - 'left' contains elements smaller than the pivot.
    # - 'middle' contains elements equal to the pivot.
    # - 'right' contains elements greater than the pivot.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply quick_sort to 'left' and 'right' sub-arrays and concatenate the results with 'middle'.
    # This will effectively sort the 'left' and 'right' sub-arrays.
    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
# Call the quick_sort function with the example array 'arr'.
sorted_arr = quick_sort(arr)
# Print the sorted array.
print(sorted_arr)
