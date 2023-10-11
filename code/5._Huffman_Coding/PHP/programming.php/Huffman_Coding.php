<?php
class HuffmanNode {
    public $data;
    public $frequency;
    public $left;
    public $right;

    function __construct($data, $frequency) {
        $this->data = $data;
        $this->frequency = $frequency;
        $this->left = null;
        $this->right = null;
    }
}

function buildHuffmanTree($freqMap) {
    $minHeap = new SplMinHeap();

    foreach ($freqMap as $char => $freq) {
        $node = new HuffmanNode($char, $freq);
        $minHeap->insert($node);
    }

    while ($minHeap->count() > 1) {
        $left = $minHeap->extract();
        $right = $minHeap->extract();

        $merged = new HuffmanNode(null, $left->frequency + $right->frequency);
        $merged->left = $left;
        $merged->right = $right;

        $minHeap->insert($merged);
    }

    return $minHeap->top();
}

function generateHuffmanCodes($root, $code, &$huffmanCodes) {
    if ($root === null) {
        return;
    }

    if ($root->data !== null) {
        $huffmanCodes[$root->data] = $code;
    }

    generateHuffmanCodes($root->left, $code . "0", $huffmanCodes);
    generateHuffmanCodes($root->right, $code . "1", $huffmanCodes);
}

function huffmanCoding($text) {
    $freqMap = [];

    for ($i = 0; $i < strlen($text); $i++) {
        $char = $text[$i];
        if (array_key_exists($char, $freqMap)) {
            $freqMap[$char]++;
        } else {
            $freqMap[$char] = 1;
        }
    }

    $root = buildHuffmanTree($freqMap);
    $huffmanCodes = [];
    generateHuffmanCodes($root, "", $huffmanCodes);

    $encodedText = "";
    for ($i = 0; $i < strlen($text); $i++) {
        $encodedText .= $huffmanCodes[$text[$i]];
    }

    return $encodedText;
}

$text = "this is an example for huffman encoding";
$encodedText = huffmanCoding($text);

echo "Huffman Codes:\n";
foreach ($huffmanCodes as $char => $code) {
    echo "$char: $code\n";
}
echo "Encoded Text: $encodedText\n";
?>