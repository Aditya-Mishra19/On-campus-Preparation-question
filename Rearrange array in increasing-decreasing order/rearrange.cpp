#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve() {
    vector<int> arr = {8, 7, 1, 2, 3, 9};
    sort(arr.begin(), arr.end());
    int n = arr.size();
    for (int i = 0; i < n / 2; ++i) {
        cout << arr[i] << " ";
    }
    for (int i = n - 1; i >= n / 2; --i) {
        cout << arr[i] << " ";
    }
}

int main() {
    solve();
    return 0;
}
