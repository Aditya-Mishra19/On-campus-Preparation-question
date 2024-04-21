#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

void solve(vector<int>& arr, int N) {
    unordered_set<int> unique;
    for (int i = 0; i < N; ++i) {
        if (unique.find(arr[i]) == unique.end()) {
            unique.insert(arr[i]);
        }
    }
    for (int num : unique) {
        cout << num << " ";
    }
}

int main() {
    vector<int> arr = {4, 4, 1, 1, 2, 2, 3, 3};
    int N = arr.size();
    solve(arr, N);
    return 0;
}
