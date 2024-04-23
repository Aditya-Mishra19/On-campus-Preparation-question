import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void solve(int[][] arr) {
        Map<Integer, Integer> store = new HashMap<>();
        for (int[] nums : arr) {
            int first = nums[0];
            int second = nums[1];
            if (!store.containsKey(second)) {
                store.put(first, second);
            } else {
                System.out.print("(" + first + ", " + second + ") ");
            }
        }
    }

    public static void main(String[] args) {
        int[][] arr = {{1, 2}, {2, 1}, {3, 4}, {4, 5}, {5, 4}};
        solve(arr);
    }
}
