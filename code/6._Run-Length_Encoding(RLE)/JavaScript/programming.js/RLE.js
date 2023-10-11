function runLengthEncode(input) {
  let encoded = "";
  let count = 1;
  for (let i = 1; i < input.length; i++) {
    if (input[i] === input[i - 1]) {
      count++;
    } else {
      encoded += input[i - 1] + count;
      count = 1;
    }
  }
  encoded += input[input.length - 1] + count;
  return encoded;
}

function runLengthDecode(encoded) {
  let decoded = "";
  for (let i = 0; i < encoded.length; i += 2) {
    let character = encoded[i];
    let count = parseInt(encoded[i + 1]);
    decoded += character.repeat(count);
  }
  return decoded;
}

const input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB";
const encoded = runLengthEncode(input);
console.log("Encoded: " + encoded);
const decoded = runLengthDecode(encoded);
console.log("Decoded: " + decoded);
