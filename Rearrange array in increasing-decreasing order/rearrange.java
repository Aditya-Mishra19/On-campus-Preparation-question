import java.util.Arrays;

public class Main {
    public static void solve() {
        int[] arr = {8, 7, 1, 2, 3, 9};
        Arrays.sort(arr);
        int n = arr.length;
        for (int i = 0; i < n / 2; ++i) {
            System.out.print(arr[i] + " ");
        }
        for (int i = n - 1; i >= n / 2; --i) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {
        solve();
    }
}
