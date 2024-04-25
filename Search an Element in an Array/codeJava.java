public class Main {
    public static void main(String args[]) {
      int arr[] = {6,7,9,5,3,10};
      int n = arr.length;
      int k = 10;
      int ans = -1;
      for (int i = 0; i < n; i++) {
        if (arr[i] == k) {
          ans = i;
          break;
        }
      }
      System.out.print("The element is present in "+ans+" index");
    }
  }
  