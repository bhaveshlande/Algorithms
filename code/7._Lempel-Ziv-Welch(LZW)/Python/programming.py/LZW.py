def compress(input_string):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    start = 0
    current_code = 256

    for i in range(1, len(input_string) + 1):
        current_substring = input_string[start:i]

        if current_substring not in dictionary and i < len(input_string):
            dictionary[current_substring] = current_code
            current_code += 1
        else:
            if i == len(input_string):
                result.append(dictionary[current_substring])
            start = i

    return result


def decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    result = [chr(compressed_data[0])]
    current_code = 256

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == current_code:
            entry = result[0]
        else:
            raise ValueError("Corrupted data")

        result.append(entry)
        dictionary[current_code] = result[0]
        current_code += 1

    return "".join(result)


# Example usage:
original_text = "ABABABABA"
compressed_data = compress(original_text)
print("Compressed Data:", compressed_data)
decompressed_text = decompress(compressed_data)
print("Decompressed Text:", decompressed_text)
