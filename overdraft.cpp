#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int bal = 0;
	int overdraft = 0;
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		bal += t;
		if (bal < 0) {
			overdraft += bal;
			bal = 0;
		}
	}
	cout << -overdraft << endl;
}