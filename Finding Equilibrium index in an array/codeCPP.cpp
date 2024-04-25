#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& arr, int N) {
    vector<int> pre(N), suf(N);
    pre[0] = arr[0];
    suf[N - 1] = arr[N - 1];
    for (int i = 1; i < N; ++i) {
        pre[i] = pre[i - 1] + arr[i];
    }
    for (int i = N - 2; i >= 0; --i) {
        suf[i] = suf[i + 1] + arr[i];
    }
    for (int i = 0; i < N; ++i) {
        if (pre[i] == suf[i]) {
            return i;
        }
    }
    return -1;
}

int solve2(vector<int>& arr, int N) {
    int total = 0;
    for (int num : arr) {
        total += num;
    }
    int left = 0, right = total;
    for (int i = 0; i < N; ++i) {
        right -= arr[i];
        if (left == right) {
            return i;
        }
        left += arr[i];
    }
    return -1;
}

int main() {
    vector<int> nums = {1, -1, 4};
    int n = nums.size();
    cout << "2. Equilibrium point: " << solve2(nums, n) << endl;
    return 0;
}
