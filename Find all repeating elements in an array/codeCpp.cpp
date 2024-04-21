#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

void solve(vector<int>& arr, int N) {
    unordered_map<int, int> store;
    for (int num : arr) {
        store[num]++;
    }
    for (auto it = store.begin(); it != store.end(); ++it) {
        cout << it->first << " ";
    }
}

int main() {
    vector<int> arr = {1, 1, 2, 2, 3, 3};
    int N = 6;
    solve(arr, N);
    return 0;
}
