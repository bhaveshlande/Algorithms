def run_length_encode(input_string):
    encoded = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded += input_string[i - 1] + str(count)
            count = 1
    encoded += input_string[-1] + str(count)
    return encoded


def run_length_decode(encoded_string):
    decoded = ""
    i = 0
    while i < len(encoded_string):
        char = encoded_string[i]
        count = int(encoded_string[i + 1])
        decoded += char * count
        i += 2
    return decoded


# Example usage:
input_str = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoded_str = run_length_encode(input_str)
print("Encoded:", encoded_str)
decoded_str = run_length_decode(encoded_str)
print("Decoded:", decoded_str)
