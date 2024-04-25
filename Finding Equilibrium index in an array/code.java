import java.util.*;

public class Main {
    static int solve(int[] arr, int N) {
        int[] pre = new int[N];
        int[] suf = new int[N];
        pre[0] = arr[0];
        suf[N - 1] = arr[N - 1];
        for (int i = 1; i < N; ++i) {
            pre[i] = pre[i - 1] + arr[i];
        }
        for (int i = N - 2; i >= 0; --i) {
            suf[i] = suf[i + 1] + arr[i];
        }
        for (int i = 0; i < N; ++i) {
            if (pre[i] == suf[i]) {
                return i;
            }
        }
        return -1;
    }

    static int solve2(int[] arr, int N) {
        int total = 0;
        for (int num : arr) {
            total += num;
        }
        int left = 0, right = total;
        for (int i = 0; i < N; ++i) {
            right -= arr[i];
            if (left == right) {
                return i;
            }
            left += arr[i];
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {1, -1, 4};
        int n = nums.length;
        System.out.println("2. Equilibrium point: " + solve2(nums, n));
    }
}
