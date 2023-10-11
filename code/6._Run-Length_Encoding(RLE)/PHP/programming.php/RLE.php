function runLengthEncode($input) {
$encoded = '';
$count = 1;
for ($i = 1; $i < strlen($input); $i++) { if ($input[$i]==$input[$i - 1]) { $count++; } else { $encoded .=$input[$i - 1]
    . $count; $count=1; } } $encoded .=$input[strlen($input) - 1] . $count; return $encoded; } function
    runLengthDecode($encoded) { $decoded='' ; $len=strlen($encoded); for ($i=0; $i < $len; $i +=2) {
    $character=$encoded[$i]; $count=(int)$encoded[$i + 1]; $decoded .=str_repeat($character, $count); } return $decoded;
    } $input="WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB" ; $encoded=runLengthEncode($input);
    echo "Encoded: " . $encoded . "\n" ; $decoded=runLengthDecode($encoded); echo "Decoded: " . $decoded . "\n" ;