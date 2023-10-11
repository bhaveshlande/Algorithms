def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.

    :param arr: The input array to be sorted.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print(my_list)
