using System;
using System.Text;

class RunLengthEncoding
{
    static string RunLengthEncode(string input)
    {
        StringBuilder encoded = new StringBuilder();
        int count = 1;
        for (int i = 1; i < input.Length; i++)
        {
            if (input[i] == input[i - 1])
            {
                count++;
            }
            else
            {
                encoded.Append(input[i - 1]).Append(count);
                count = 1;
            }
        }
        encoded.Append(input[input.Length - 1]).Append(count);
        return encoded.ToString();
    }

    static string RunLengthDecode(string encoded)
    {
        StringBuilder decoded = new StringBuilder();
        for (int i = 0; i < encoded.Length; i += 2)
        {
            char character = encoded[i];
            int count = int.Parse(encoded[i + 1].ToString());
            decoded.Append(character, count);
        }
        return decoded.ToString();
    }

    static void Main(string[] args)
    {
        string input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB";
        string encoded = RunLengthEncode(input);
        Console.WriteLine("Encoded: " + encoded);
        string decoded = RunLengthDecode(encoded);
        Console.WriteLine("Decoded: " + decoded);
    }
}
