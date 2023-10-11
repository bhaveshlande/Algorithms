#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> compress(const std::string &input)
{
    std::unordered_map<std::string, int> dictionary;
    for (int i = 0; i < 256; i++)
    {
        dictionary[std::string(1, char(i))] = i;
    }

    std::vector<int> result;
    int start = 0;
    int currentCode = 256;

    for (int i = 1; i <= input.size(); i++)
    {
        std::string currentSubstring = input.substr(start, i - start);

        if (dictionary.find(currentSubstring) == dictionary.end() && i < input.size())
        {
            dictionary[currentSubstring] = currentCode;
            currentCode++;
        }
        else
        {
            if (i == input.size())
            {
                result.push_back(dictionary[currentSubstring]);
            }
            start = i;
        }
    }

    return result;
}

std::string decompress(const std::vector<int> &compressedData)
{
    std::unordered_map<int, std::string> dictionary;
    for (int i = 0; i < 256; i++)
    {
        dictionary[i] = std::string(1, char(i));
    }

    std::vector<std::string> result;
    result.push_back(dictionary[compressedData[0]]);
    int currentCode = 256;

    for (size_t i = 1; i < compressedData.size(); i++)
    {
        int code = compressedData[i];
        std::string entry;

        if (dictionary.find(code) != dictionary.end())
        {
            entry = dictionary[code];
        }
        else if (code == currentCode)
        {
            entry = result[0];
        }
        else
        {
            throw std::invalid_argument("Corrupted data");
        }

        result.push_back(entry);
        dictionary[currentCode] = result[0];
        currentCode++;
    }

    std::string decompressedText;
    for (const std::string &s : result)
    {
        decompressedText += s;
    }

    return decompressedText;
}

int main()
{
    std::string originalText = "ABABABABA";
    std::vector<int> compressedData = compress(originalText);
    std::cout << "Compressed Data: ";
    for (int code : compressedData)
    {
        std::cout << code << " ";
    }
    std::cout << std::endl;
    std::string decompressedText = decompress(compressedData);
    std::cout << "Decompressed Text: " << decompressedText << std::endl;
    return 0;
}
