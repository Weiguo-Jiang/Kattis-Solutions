#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> v;
	int min = 1000000001;
	for (int i = 0; i < n; i++) {
		int k;
		cin >> k;
		if (k < min) {
			min = k;
		}
		v.push_back(k);
	}

	for (int i = 0; i < n; i++) {
		if (v[i] == min) {
			cout << i << endl;
			return 0;
		}
	}
}