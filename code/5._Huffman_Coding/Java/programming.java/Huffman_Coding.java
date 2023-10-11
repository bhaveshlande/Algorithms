import java.util.PriorityQueue;
import java.util.HashMap;
import java.util.Map;

class HuffmanNode implements Comparable<HuffmanNode> {
    char data;
    int frequency;
    HuffmanNode left, right;

    public int compareTo(HuffmanNode node) {
        return frequency - node.frequency;
    }
}

public class HuffmanCoding {
    public static HuffmanNode buildHuffmanTree(Map<Character, Integer> freqMap) {
        PriorityQueue<HuffmanNode> heap = new PriorityQueue<>();

        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            HuffmanNode node = new HuffmanNode();
            node.data = entry.getKey();
            node.frequency = entry.getValue();
            heap.add(node);
        }

        while (heap.size() > 1) {
            HuffmanNode left = heap.poll();
            HuffmanNode right = heap.poll();

            HuffmanNode merged = new HuffmanNode();
            merged.frequency = left.frequency + right.frequency;
            merged.left = left;
            merged.right = right;

            heap.add(merged);
        }

        return heap.poll();
    }

    public static void generateHuffmanCodes(HuffmanNode root, String code, Map<Character, String> huffmanCodes) {
        if (root == null)
            return;
        if (root.left == null && root.right == null) {
            huffmanCodes.put(root.data, code);
        }
        generateHuffmanCodes(root.left, code + "0", huffmanCodes);
        generateHuffmanCodes(root.right, code + "1", huffmanCodes);
    }

    public static String huffmanCoding(String text) {
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : text.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        HuffmanNode root = buildHuffmanTree(freqMap);
        Map<Character, String> huffmanCodes = new HashMap<>();
        generateHuffmanCodes(root, "", huffmanCodes);

        StringBuilder encodedText = new StringBuilder();
        for (char c : text.toCharArray()) {
            encodedText.append(huffmanCodes.get(c));
        }

        return encodedText.toString();
    }

    public static void main(String[] args) {
        String text = "this is an example for huffman encoding";
        String encodedText = huffmanCoding(text);
        System.out.println("Huffman Codes:");
        for (Map.Entry<Character, String> entry : huffmanCodes.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("Encoded Text: " + encodedText);
    }
}
