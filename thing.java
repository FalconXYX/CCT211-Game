import java.util.Arrays;

public class MinimumCharacters {

    public static int[] countMinimumCharacters(String s, String[] arr) {
        int n = s.length();
        int m = arr.length;
        int[] result = new int[m];

        // Count occurrences of each digit in the special string
        int[] charCount = new int[10];
        for (char c : s.toCharArray()) {
            charCount[c - '0']++;
        }

        for (int i = 0; i < m; i++) {
            // Count occurrences of each digit in the current string to construct
            int[] currentCount = new int[10];
            for (char c : arr[i].toCharArray()) {
                currentCount[c - '0']++;
            }

            // Check if the string can be constructed
            boolean canConstruct = true;
            for (int j = 0; j < 10; j++) {
                if (currentCount[j] > charCount[j]) {
                    canConstruct = false;
                    break;
                }
            }

            // If the string can be constructed, calculate the minimum length
            if (canConstruct) {
                int minLength = Integer.MAX_VALUE;
                for (char c : arr[i].toCharArray()) {
                    minLength = Math.min(minLength, charCount[c - '0']);
                }
                result[i] = minLength;
            } else {
                // If the string cannot be constructed, set the result to -1
                result[i] = -1;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String s = "064819848398";
        String[] arr = {"088", "364", "07"};

        int[] result = countMinimumCharacters(s, arr);
        System.out.println(Arrays.toString(result));
    }
}
