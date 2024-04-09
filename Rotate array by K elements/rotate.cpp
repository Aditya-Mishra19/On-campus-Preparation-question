#include <iostream>
#include <vector>
using namespace std;

void leftToRightrotateArray(vector<int> arr, int k, int N) {
    vector<int> ans(N);
    for (int i = 0; i < N; ++i) {
        ans[i] = arr[(i + k) % N];
    }
    for (int i = 0; i < N; ++i) {
        cout << ans[i] << " ";
    }
}


// Homework
void Right2LeftrotateArray(vector<int> arr, int k, int N) {
    vector<int> ans(N);
    for (int i = 0; i < N; ++i) {
        ans[(i + k) % N] = arr[i];  	    // small change just put formula to LHS
    }
    for (int i = 0; i < N; ++i) {
        cout << ans[i] << " ";
    }
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    int N = arr.size();
    int k = 2;
    leftToRightrotateArray(arr, k, N);
    Right2LeftrotateArray(arr, k, N);
    return 0;
}
