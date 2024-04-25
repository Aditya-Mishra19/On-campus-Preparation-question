#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n = 6;
	int arr[n] = {6, 7, 9, 5, 3, 10};
	int k = 10;
	int ans = -1;
	for (int i = 0; i < n; i++) {
		if (arr[i] == k) {
			ans = i;
			break;
		}
	}
	cout <<"The element is present in " <<ans<<" index";
}
