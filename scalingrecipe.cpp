#include <iostream>

using namespace std;

int main() {
	int n, x, y;
	cin >> n >> x >> y;
	for (int i = 0; i < n; i++) {
		int k;
		cin >> k;
		cout << k * y / x << endl;
	}
}