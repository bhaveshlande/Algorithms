function bubbleSort(arr) {
  /**
   * Sorts an array using the Bubble Sort algorithm.
   *
   * @param arr The input array to be sorted.
   */
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // Swap arr[j] and arr[j+1]
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
}

const myArray = [64, 34, 25, 12, 22, 11, 90];
bubbleSort(myArray);
console.log(myArray);
