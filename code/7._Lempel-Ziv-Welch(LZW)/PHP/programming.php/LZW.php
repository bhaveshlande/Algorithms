<?php
function compress($input) {
    $dictionary = [];
    for ($i = 0; $i < 256; $i++) {
        $dictionary[chr($i)] = $i;
    }

    $result = [];
    $start = 0;
    $currentCode = 256;

    for ($i = 1; $i <= strlen($input); $i++) {
        $currentSubstring = substr($input, $start, $i - $start);

        if (!array_key_exists($currentSubstring, $dictionary) && $i < strlen($input)) {
            $dictionary[$currentSubstring] = $currentCode;
            $currentCode++;
        } else {
            if ($i == strlen($input)) {
                $result[] = $dictionary[$currentSubstring];
            }
            $start = $i;
        }
    }

    return $result;
}

function decompress($compressedData) {
    $dictionary = [];
    for ($i = 0; $i < 256; $i++) {
        $dictionary[$i] = chr($i);
    }

    $result = [$dictionary[$compressedData[0]]];
    $currentCode = 256;

    for ($i = 1; $i < count($compressedData); $i++) {
        $code = $compressedData[$i];
        $entry = '';

        if (array_key_exists($code, $dictionary)) {
            $entry = $dictionary[$code];
        } elseif ($code == $currentCode) {
            $entry = $result[0];
        } else {
            throw new Exception("Corrupted data");
        }

        $result[] = $entry;
        $dictionary[$currentCode] = $result[0];
        $currentCode++;
    }

    return implode('', $result);
}

$originalText = "ABABABABA";
$compressedData = compress($originalText);
echo "Compressed Data: " . implode(' ', $compressedData) . PHP_EOL;
$decompressedText = decompress($compressedData);
echo "Decompressed Text: " . $decompressedText . PHP_EOL;
?>