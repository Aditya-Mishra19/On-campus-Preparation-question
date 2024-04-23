import java.util.*;

public class Main {
    static void solve(int[] arr) {
        Map<Integer, Integer> store = new HashMap<>();
        for (int num : arr) {
            store.put(num, store.getOrDefault(num, 0) + 1);
        }
        List<Map.Entry<Integer, Integer>> ans = new ArrayList<>(store.entrySet());
        Collections.sort(ans, (a, b) -> b.getValue() - a.getValue());
        System.out.println("Sorted by frequency:");
        for (Map.Entry<Integer, Integer> entry : ans) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5, 0};
        solve(arr);
    }
}
