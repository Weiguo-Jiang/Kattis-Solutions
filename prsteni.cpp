#include <iostream>
#include <vector>

using namespace std;

int simplify(int n, int d) {
	int k = min(n, d);
	int m = 0;
	for (int i = 1; i <= k; i++) {
		if (n % i == 0 && d % i == 0 && i > m) {
			m = i;
		}
	}
	
	cout << n/m << "/" << d/m << endl;

	return 0;
}

int main() {
	int N;
	cin >> N;
	vector<int> radii;
	for (int i = 0; i < N; i++) {
		int r;
		cin >> r;
		radii.push_back(r);
	}

	for (int i = 1; i < N; i++) {
		simplify(radii[0], radii[i]);
	}
}