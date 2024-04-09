public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 5, 6, 8};
        int ans = 0;
        for (int num : arr) {
            ans += num;
        }
        System.out.println("Sum of array is: " + ans);
    }
}
