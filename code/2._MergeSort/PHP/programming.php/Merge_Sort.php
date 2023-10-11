function mergeSort(&$arr) {
$n = count($arr);
if ($n < 2) { return; } $mid=(int)($n / 2); $left=array_slice($arr, 0, $mid); $right=array_slice($arr, $mid);
    mergeSort($left); mergeSort($right); merge($arr, $left, $right); } function merge(&$arr, $left, $right) {
    $i=$j=$k=0; $leftLength=count($left); $rightLength=count($right); while ($i < $leftLength && $j < $rightLength) { if
    ($left[$i] <=$right[$j]) { $arr[$k]=$left[$i]; $i++; } else { $arr[$k]=$right[$j]; $j++; } $k++; } while ($i <
    $leftLength) { $arr[$k]=$left[$i]; $i++; $k++; } while ($j < $rightLength) { $arr[$k]=$right[$j]; $j++; $k++; } }
    $arr=[3, 6, 8, 10, 1, 2, 1]; mergeSort($arr); foreach ($arr as $num) { echo $num . " " ; }