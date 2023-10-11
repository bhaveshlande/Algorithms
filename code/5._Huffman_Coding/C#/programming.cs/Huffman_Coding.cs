using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class HuffmanNode : IComparable<HuffmanNode>
{
    public char Data { get; set; }
    public int Frequency { get; set; }
    public HuffmanNode Left { get; set; }
    public HuffmanNode Right { get; set; }

    public int CompareTo(HuffmanNode other)
    {
        return Frequency - other.Frequency;
    }
}

class HuffmanCoding
{
    public static HuffmanNode BuildHuffmanTree(Dictionary<char, int> freqMap)
    {
        var minHeap = new PriorityQueue<HuffmanNode>();

        foreach (var entry in freqMap)
        {
            minHeap.Enqueue(new HuffmanNode { Data = entry.Key, Frequency = entry.Value });
        }

        while (minHeap.Count > 1)
        {
            var left = minHeap.Dequeue();
            var right = minHeap.Dequeue();

            var merged = new HuffmanNode { Frequency = left.Frequency + right.Frequency, Left = left, Right = right };

            minHeap.Enqueue(merged);
        }

        return minHeap.Dequeue();
    }

    public static void GenerateHuffmanCodes(HuffmanNode root, string code, Dictionary<char, string> huffmanCodes)
    {
        if (root == null)
            return;
        if (root.Left == null && root.Right == null)
        {
            huffmanCodes[root.Data] = code;
        }
        GenerateHuffmanCodes(root.Left, code + "0", huffmanCodes);
        GenerateHuffmanCodes(root.Right, code + "1", huffmanCodes);
    }

    public static string HuffmanCoding(string text)
    {
        var freqMap = new Dictionary<char, int>();
        foreach (var c in text)
        {
            if (freqMap.ContainsKey(c))
                freqMap[c]++;
            else
                freqMap[c] = 1;
        }

        var root = BuildHuffmanTree(freqMap);
        var huffmanCodes = new Dictionary<char, string>();
        GenerateHuffmanCodes(root, "", huffmanCodes);

        var encodedText = new StringBuilder();
        foreach (var c in text)
        {
            encodedText.Append(huffmanCodes[c]);
        }

        return encodedText.ToString();
    }

    public static void Main()
    {
        var text = "this is an example for huffman encoding";
        var encodedText = HuffmanCoding(text);
        Console.WriteLine("Huffman Codes:");
        foreach (var entry in huffmanCodes)
        {
            Console.WriteLine(entry.Key + ": " + entry.Value);
        }
        Console.WriteLine("Encoded Text: " + encodedText);
    }
}
