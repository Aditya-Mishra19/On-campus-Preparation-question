#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr = {1, 2, 3, 5, 6, 8};
    int ans = 0;
    for (int num : arr) {
        ans += num;
    }
    cout << "Sum of array is: " << ans << endl;
    return 0;
}
