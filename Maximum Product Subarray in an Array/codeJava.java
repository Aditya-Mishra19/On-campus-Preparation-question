public class Main {
    static void solve(int[] arr, int n) {
        int maxP = 0;
        int sufx = 1, prex = 1;
        for (int i = 0; i < n; i++) {
            if (arr[i] == arr[n - i - 1] && arr[i] == 0) {
                sufx = 1;
                prex = 1;
            } else {
                prex *= arr[i];
                sufx *= arr[n - i - 1];
            }
            maxP = Math.max(maxP, Math.max(prex, sufx));
        }
        System.out.println("Maximum Product: " + maxP);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, -3, 0, -4, -5};
        int N = arr.length;
        solve(arr, N);
    }
}
