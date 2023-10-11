import heapq
from collections import defaultdict


# Node class to build the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Function to build the Huffman tree
def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


# Function to generate Huffman codes
def generate_huffman_codes(root, code, huffman_codes):
    if root is None:
        return
    if root.char is not None:
        huffman_codes[root.char] = code
    generate_huffman_codes(root.left, code + "0", huffman_codes)
    generate_huffman_codes(root.right, code + "1", huffman_codes)


# Function to perform Huffman coding
def huffman_coding(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1

    root = build_huffman_tree(freq_map)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)

    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, root


# Example usage:
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    encoded_text, root = huffman_coding(text)
    print("Huffman Codes:")
    for char, code in sorted(huffman_codes.items()):
        print(f"{char}: {code}")
    print("Encoded Text:", encoded_text)
