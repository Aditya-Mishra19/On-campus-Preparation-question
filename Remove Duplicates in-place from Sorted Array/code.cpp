#include <iostream>
#include <vector>
using namespace std;

void solve(vector<int>& arr, int N) {
    int i = 0;
    for (int j = 1; j < N; ++j) {
        if (arr[i] != arr[j]) {
            ++i;
            arr[i] = arr[j];
        }
    }
    for (int k = 0; k <= i; ++k) {
        cout << arr[k] << " ";
    }
}

int main() {
    vector<int> arr = {1, 2, 2, 2, 3};
    int N = arr.size();
    solve(arr, N);
    return 0;
}
