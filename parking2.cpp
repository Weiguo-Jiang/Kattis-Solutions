#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int m;
		cin >> m;
		int max = -1;
		int min = 101;
		for (int j = 0; j < m; j++) {
			int k;
			cin >> k;
			if (k > max) {
				max = k;
			}
			if (k < min) {
				min = k;
			}
		}
		cout << 2*(max - min) << endl;
	}
}