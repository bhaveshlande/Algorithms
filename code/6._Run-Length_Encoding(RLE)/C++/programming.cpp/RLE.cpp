#include <iostream>
#include <string>
using namespace std;

string runLengthEncode(string input)
{
    string encoded = "";
    int count = 1;
    for (int i = 1; i < input.length(); i++)
    {
        if (input[i] == input[i - 1])
        {
            count++;
        }
        else
        {
            encoded += input[i - 1] + to_string(count);
            count = 1;
        }
    }
    encoded += input[input.length() - 1] + to_string(count);
    return encoded;
}

string runLengthDecode(string encoded)
{
    string decoded = "";
    for (int i = 0; i < encoded.length(); i += 2)
    {
        char character = encoded[i];
        int count = encoded[i + 1] - '0';
        for (int j = 0; j < count; j++)
        {
            decoded += character;
        }
    }
    return decoded;
}

int main()
{
    string input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB";
    string encoded = runLengthEncode(input);
    cout << "Encoded: " << encoded << endl;
    string decoded = runLengthDecode(encoded);
    cout << "Decoded: " << decoded << endl;
    return 0;
}
