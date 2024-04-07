#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

void getFreq(const vector<int>& arr) {
    unordered_map<int, int> store;
    for (int num : arr) {
        store[num]++;
    }

    for (const auto& entry : store) {
        cout << entry.first << " " << entry.second << endl;
    }
}

int main() {
    vector<int> arr = {10, 5, 15, 10, 5};
    getFreq(arr);
    return 0;
}
