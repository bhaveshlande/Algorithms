import java.util.*;

public class LZWCompression {
    public static List<Integer> compress(String input) {
        Map<String, Integer> dictionary = new HashMap<>();
        for (int i = 0; i < 256; i++) {
            dictionary.put(Character.toString((char) i), i);
        }

        List<Integer> result = new ArrayList<>();
        int start = 0;
        int currentCode = 256;

        for (int i = 1; i <= input.length(); i++) {
            String currentSubstring = input.substring(start, i);

            if (!dictionary.containsKey(currentSubstring) && i < input.length()) {
                dictionary.put(currentSubstring, currentCode);
                currentCode++;
            } else {
                if (i == input.length()) {
                    result.add(dictionary.get(currentSubstring));
                }
                start = i;
            }
        }

        return result;
    }

    public static String decompress(List<Integer> compressedData) {
        Map<Integer, String> dictionary = new HashMap<>();
        for (int i = 0; i < 256; i++) {
            dictionary.put(i, Character.toString((char) i));
        }

        List<String> result = new ArrayList<>();
        result.add(dictionary.get(compressedData.get(0)));
        int currentCode = 256;

        for (int i = 1; i < compressedData.size(); i++) {
            int code = compressedData.get(i);
            String entry;

            if (dictionary.containsKey(code)) {
                entry = dictionary.get(code);
            } else if (code == currentCode) {
                entry = result.get(0);
            } else {
                throw new IllegalArgumentException("Corrupted data");
            }

            result.add(entry);
            dictionary.put(currentCode, result.get(0));
            currentCode++;
        }

        StringBuilder sb = new StringBuilder();
        for (String s : result) {
            sb.append(s);
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String originalText = "ABABABABA";
        List<Integer> compressedData = compress(originalText);
        System.out.println("Compressed Data: " + compressedData);
        String decompressedText = decompress(compressedData);
        System.out.println("Decompressed Text: " + decompressedText);
    }
}
