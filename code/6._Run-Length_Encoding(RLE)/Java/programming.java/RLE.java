public class RunLengthEncoding {
    public static String runLengthEncode(String input) {
        StringBuilder encoded = new StringBuilder();
        int count = 1;
        for (int i = 1; i < input.length(); i++) {
            if (input.charAt(i) == input.charAt(i - 1)) {
                count++;
            } else {
                encoded.append(input.charAt(i - 1)).append(count);
                count = 1;
            }
        }
        encoded.append(input.charAt(input.length() - 1)).append(count);
        return encoded.toString();
    }

    public static String runLengthDecode(String encoded) {
        StringBuilder decoded = new StringBuilder();
        for (int i = 0; i < encoded.length(); i += 2) {
            char character = encoded.charAt(i);
            int count = Integer.parseInt(String.valueOf(encoded.charAt(i + 1));
            for (int j = 0; j < count; j++) {
                decoded.append(character);
            }
        }
        return decoded.toString();
    }

    public static void main(String[] args) {
        String input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB";
        String encoded = runLengthEncode(input);
        System.out.println("Encoded: " + encoded);
        String decoded = runLengthDecode(encoded);
        System.out.println("Decoded: " + decoded);
    }
}
