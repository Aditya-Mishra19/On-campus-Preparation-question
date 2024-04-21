import java.util.Arrays;

public class Main {
    public static void solve(int[] arr, int N) {
        int i = 0;
        for (int j = 1; j < N; ++j) {
            if (arr[i] != arr[j]) {
                ++i;
                arr[i] = arr[j];
            }
        }
        for (int k = 0; k <= i; ++k) {
            System.out.print(arr[k] + " ");
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 2, 3};
        int N = arr.length;
        solve(arr, N);
    }
}
