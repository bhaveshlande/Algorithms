function quickSort(&$arr, $low, $high) {
if ($low < $high) { $pivotIndex=partition($arr, $low, $high); quickSort($arr, $low, $pivotIndex - 1); quickSort($arr,
    $pivotIndex + 1, $high); } } function partition(&$arr, $low, $high) { $pivot=$arr[$high]; $i=$low - 1; for ($j=$low;
    $j < $high; $j++) { if ($arr[$j] < $pivot) { $i++; $temp=$arr[$i]; $arr[$i]=$arr[$j]; $arr[$j]=$temp; } }
    $temp=$arr[$i + 1]; $arr[$i + 1]=$arr[$high]; $arr[$high]=$temp; return $i + 1; } $arr=[3, 6, 8, 10, 1, 2, 1];
    quickSort($arr, 0, count($arr) - 1); foreach ($arr as $num) { echo $num . " " ; }