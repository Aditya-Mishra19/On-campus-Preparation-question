public class Main {
    public static void left2RightrotateArray(int[] arr, int k, int N) {
        int[] ans = new int[N];
        for (int i = 0; i < N; i++) {
            ans[i] = arr[(i + k) % N];
        }
        for (int i = 0; i < N; i++) {
            System.out.print(ans[i] + " ");
        }
    }
    public static void Right2LeftrotateArray(int[] arr, int k, int N) {
        int[] ans = new int[N];
        for (int i = 0; i < N; i++) {
            ans[(i + k) % N] = arr[i];      // small change just put formula to LHS
        }
        for (int i = 0; i < N; i++) {
            System.out.print(ans[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int N = arr.length;
        int k = 2;
        left2RightrotateArray(arr, k, N);
        Right2LeftrotateArray(arr, k, N);
    }
}
