#include <iostream>
#include <vector>

using namespace std;

void getReverse(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    getReverse(arr);
    return 0;
}
