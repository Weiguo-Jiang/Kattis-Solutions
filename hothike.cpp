#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> v;
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		v.push_back(t);
	}

	int maximum = 100;
	int index = 0;

	for (int i = 0; i < n-2; i++) {
		int localMax = max(v[i], v[i+2]);
		if (localMax < maximum) {
			maximum = localMax;
			index = i+1;
		}
	}
	cout << index << " " << maximum << endl;
}