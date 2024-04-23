#include <iostream>
#include <algorithm>

using namespace std;

void solve(int arr[], int n) {
    int maxP = 0;
    int sufx = 1, prex = 1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == arr[n - i - 1] && arr[i] == 0) {
            sufx = 1;
            prex = 1;
        } else {
            prex *= arr[i];
            sufx *= arr[n - i - 1];
        }
        maxP = max(maxP, max(prex, sufx));
    }
    cout << "Maximum Product: " << maxP << endl;
}

int main() {
    int arr[] = {1, 2, -3, 0, -4, -5};
    int N = sizeof(arr) / sizeof(arr[0]);
    solve(arr, N);
    return 0;
}
