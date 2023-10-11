#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

struct HuffmanNode
{
    char data;
    int frequency;
    HuffmanNode *left;
    HuffmanNode *right;

    HuffmanNode(char data, int frequency) : data(data), frequency(frequency), left(nullptr), right(nullptr) {}

    bool operator>(const HuffmanNode &other) const
    {
        return frequency > other.frequency;
    }
};

HuffmanNode *buildHuffmanTree(const std::unordered_map<char, int> &freqMap)
{
    std::priority_queue<HuffmanNode, std::vector<HuffmanNode>, std::greater<HuffmanNode>> minHeap;

    for (const auto &entry : freqMap)
    {
        minHeap.push(HuffmanNode(entry.first, entry.second));
    }

    while (minHeap.size() > 1)
    {
        HuffmanNode *left = new HuffmanNode(0, 0);
        HuffmanNode *right = new HuffmanNode(0, 0);

        *left = minHeap.top();
        minHeap.pop();
        *right = minHeap.top();
        minHeap.pop();

        HuffmanNode *merged = new HuffmanNode(0, left->frequency + right->frequency);
        merged->left = left;
        merged->right = right;

        minHeap.push(*merged);
        delete merged;
    }

    return new HuffmanNode(0, minHeap.top().frequency, minHeap.top().left, minHeap.top().right);
}

void generateHuffmanCodes(const HuffmanNode *root, std::string code, std::unordered_map<char, std::string> &huffmanCodes)
{
    if (!root)
    {
        return;
    }

    if (!root->left && !root->right)
    {
        huffmanCodes[root->data] = code;
    }

    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

std::string huffmanCoding(const std::string &text)
{
    std::unordered_map<char, int> freqMap;

    for (char c : text)
    {
        freqMap[c]++;
    }

    HuffmanNode *root = buildHuffmanTree(freqMap);
    std::unordered_map<char, std::string> huffmanCodes;

    generateHuffmanCodes(root, "", huffmanCodes);

    std::string encodedText;

    for (char c : text)
    {
        encodedText += huffmanCodes[c];
    }

    return encodedText;
}

int main()
{
    std::string text = "this is an example for huffman encoding";
    std::string encodedText = huffmanCoding(text);
    std::cout << "Huffman Codes:" << std::endl;
    for (const auto &entry : huffmanCodes)
    {
        std::cout << entry.first << ": " << entry.second << std::endl;
    }
    std::cout << "Encoded Text: " << encodedText << std::endl;
    return 0;
}
