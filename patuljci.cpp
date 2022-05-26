#include <iostream>
#include <vector>

using namespace std;

int main() {
	int sum = 0;
	vector<int> v;
	for (int i = 0; i < 9; i++) {
		int n;
		cin >> n;
		sum += n;
		v.push_back(n);
	}

	for (int i = 0; i < 9; i++) {
		for (int j = i+1; j < 9; j++) {
			if (v[i] + v[j] == sum - 100) {
				for (int k = 0; k < 9; k++) {
					if (v[k] != v[i] && v[k] != v[j]) {
						cout << v[k] << endl;
					}
				}
			}
		}
	}
}