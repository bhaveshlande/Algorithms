using System;
using System.Collections.Generic;

public class LZWCompression
{
    public static List<int> Compress(string input)
    {
        Dictionary<string, int> dictionary = new Dictionary<string, int>();
        for (int i = 0; i < 256; i++)
        {
            dictionary[Convert.ToChar(i).ToString()] = i;
        }

        List<int> result = new List<int>();
        int start = 0;
        int currentCode = 256;

        for (int i = 1; i <= input.Length; i++)
        {
            string currentSubstring = input.Substring(start, i - start);

            if (!dictionary.ContainsKey(currentSubstring) && i < input.Length)
            {
                dictionary[currentSubstring] = currentCode;
                currentCode++;
            }
            else
            {
                if (i == input.Length)
                {
                    result.Add(dictionary[currentSubstring]);
                }
                start = i;
            }
        }

        return result;
    }

    public static string Decompress(List<int> compressedData)
    {
        Dictionary<int, string> dictionary = new Dictionary<int, string>();
        for (int i = 0; i < 256; i++)
        {
            dictionary[i] = Convert.ToChar(i).ToString();
        }

        List<string> result = new List<string>();
        result.Add(dictionary[compressedData[0]]);
        int currentCode = 256;

        for (int i = 1; i < compressedData.Count; i++)
        {
            int code = compressedData[i];
            string entry;

            if (dictionary.ContainsKey(code))
            {
                entry = dictionary[code];
            }
            else if (code == currentCode)
            {
                entry = result[0];
            }
            else
            {
                throw new ArgumentException("Corrupted data");
            }

            result.Add(entry);
            dictionary[currentCode] = result[0];
            currentCode++;
        }

        return string.Join("", result);
    }

    static void Main()
    {
        string originalText = "ABABABABA";
        List<int> compressedData = Compress(originalText);
        Console.Write("Compressed Data: ");
        foreach (int code in compressedData)
        {
            Console.Write(code + " ");
        }
        Console.WriteLine();
        string decompressedText = Decompress(compressedData);
        Console.WriteLine("Decompressed Text: " + decompressedText);
    }
}
