function binarySearch($arr, $target) {
$left = 0;
$right = count($arr) - 1;

while ($left <= $right) { $mid=$left + floor(($right - $left) / 2); if ($arr[$mid]==$target) { return $mid; } elseif
    ($arr[$mid] < $target) { $left=$mid + 1; } else { $right=$mid - 1; } } return -1; // Target not found } $arr=[1, 3,
    5, 7, 9, 11, 13]; $target=7; $result=binarySearch($arr, $target); if ($result !=-1) {
    echo "Target $target found at index $result\n" ; } else { echo "Target not found\n" ; }