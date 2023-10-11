class HuffmanNode {
  constructor(data, frequency) {
    this.data = data;
    this.frequency = frequency;
    this.left = null;
    this.right = null;
  }
}

function buildHuffmanTree(freqMap) {
  const minHeap = new PriorityQueue((a, b) => a.frequency - b.frequency);

  for (const [char, freq] of Object.entries(freqMap)) {
    const node = new HuffmanNode(char, freq);
    minHeap.enqueue(node);
  }

  while (minHeap.size() > 1) {
    const left = minHeap.dequeue();
    const right = minHeap.dequeue();

    const merged = new HuffmanNode(null, left.frequency + right.frequency);
    merged.left = left;
    merged.right = right;

    minHeap.enqueue(merged);
  }

  return minHeap.peek();
}

function generateHuffmanCodes(root, code, huffmanCodes) {
  if (root === null) {
    return;
  }

  if (root.data !== null) {
    huffmanCodes[root.data] = code;
  }

  generateHuffmanCodes(root.left, code + "0", huffmanCodes);
  generateHuffmanCodes(root.right, code + "1", huffmanCodes);
}

function huffmanCoding(text) {
  const freqMap = {};

  for (const char of text) {
    freqMap[char] = (freqMap[char] || 0) + 1;
  }

  const root = buildHuffmanTree(freqMap);
  const huffmanCodes = {};
  generateHuffmanCodes(root, "", huffmanCodes);

  let encodedText = "";

  for (const char of text) {
    encodedText += huffmanCodes[char];
  }

  return encodedText;
}

class PriorityQueue {
  constructor(comparator) {
    this.elements = [];
    this.comparator = comparator || ((a, b) => a - b);
  }

  enqueue(element) {
    this.elements.push(element);
    this.bubbleUp();
  }

  dequeue() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty");
    }

    const top = this.elements[0];
    const bottom = this.elements.pop();

    if (!this.isEmpty()) {
      this.elements[0] = bottom;
      this.sinkDown();
    }

    return top;
  }

  peek() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty");
    }

    return this.elements[0];
  }

  size() {
    return this.elements.length;
  }

  isEmpty() {
    return this.elements.length === 0;
  }

  bubbleUp() {
    let index = this.elements.length - 1;

    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);

      if (
        this.comparator(this.elements[index], this.elements[parentIndex]) >= 0
      ) {
        break;
      }

      this.swap(index, parentIndex);
      index = parentIndex;
    }
  }

  sinkDown() {
    let index = 0;

    while (true) {
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;
      let smallest = index;

      if (
        leftChildIndex < this.elements.length &&
        this.comparator(
          this.elements[leftChildIndex],
          this.elements[smallest]
        ) < 0
      ) {
        smallest = leftChildIndex;
      }

      if (
        rightChildIndex < this.elements.length &&
        this.comparator(
          this.elements[rightChildIndex],
          this.elements[smallest]
        ) < 0
      ) {
        smallest = rightChildIndex;
      }

      if (smallest === index) {
        break;
      }

      this.swap(index, smallest);
      index = smallest;
    }
  }

  swap(a, b) {
    [this.elements[a], this.elements[b]] = [this.elements[b], this.elements[a]];
  }
}

const text = "this is an example for huffman encoding";
const encodedText = huffmanCoding(text);

console.log("Huffman Codes:");
for (const char in huffmanCodes) {
  console.log(`${char}: ${huffmanCodes[char]}`);
}
console.log(`Encoded Text: ${encodedText}`);
