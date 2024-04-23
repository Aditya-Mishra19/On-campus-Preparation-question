#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

void solve(vector<vector<int>>& arr) {
    unordered_map<int, int> store;
    for (const auto& nums : arr) {
        int first = nums[0];
        int second = nums[1];
        if (store.find(second) == store.end()) {
            store[first] = second;
        } else {
            cout << "(" << first << ", " << second << ") ";
        }
    }
}

int main() {
    vector<vector<int>> arr = {{1, 2}, {2, 1}, {3, 4}, {4, 5}, {5, 4}};
    solve(arr);
    return 0;
}
