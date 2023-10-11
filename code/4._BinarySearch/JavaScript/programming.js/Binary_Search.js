function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1; // Target not found
}

const myArray = [1, 3, 5, 7, 9, 11, 13];
const target = 7;
const result = binarySearch(myArray, target);

if (result !== -1) {
  console.log(`Target ${target} found at index ${result}`);
} else {
  console.log("Target not found");
}
