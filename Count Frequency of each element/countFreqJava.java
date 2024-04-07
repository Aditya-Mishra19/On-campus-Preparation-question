import java.util.HashMap;
import java.util.Map;

public class FrequencyCounter {

    public static void getFreq(int[] arr) {
        Map<Integer, Integer> store = new HashMap<>();
        for (int num : arr) {
            store.put(num, store.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : store.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        int[] arr = {10, 5, 15, 10, 5};
        getFreq(arr);
    }
}
