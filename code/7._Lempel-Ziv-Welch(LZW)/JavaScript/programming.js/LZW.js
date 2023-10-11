function compress(input) {
  const dictionary = {};
  for (let i = 0; i < 256; i++) {
    dictionary[String.fromCharCode(i)] = i;
  }

  const result = [];
  let start = 0;
  let currentCode = 256;

  for (let i = 1; i <= input.length; i++) {
    const currentSubstring = input.substring(start, i);

    if (!dictionary[currentSubstring] && i < input.length) {
      dictionary[currentSubstring] = currentCode;
      currentCode++;
    } else {
      if (i === input.length) {
        result.push(dictionary[currentSubstring]);
      }
      start = i;
    }
  }

  return result;
}

function decompress(compressedData) {
  const dictionary = {};
  for (let i = 0; i < 256; i++) {
    dictionary[i] = String.fromCharCode(i);
  }

  const result = [dictionary[compressedData[0]]];
  let currentCode = 256;

  for (let i = 1; i < compressedData.length; i++) {
    const code = compressedData[i];
    let entry = "";

    if (dictionary[code]) {
      entry = dictionary[code];
    } else if (code === currentCode) {
      entry = result[0];
    } else {
      throw new Error("Corrupted data");
    }

    result.push(entry);
    dictionary[currentCode] = result[0];
    currentCode++;
  }

  return result.join("");
}

const originalText = "ABABABABA";
const compressedData = compress(originalText);
console.log("Compressed Data: " + compressedData.join(" "));
const decompressedText = decompress(compressedData);
console.log("Decompressed Text: " + decompressedText);
