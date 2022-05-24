#include <iostream>

using namespace std;

int digitProduct(int& n) {
	int p = 1;
	while (n != 0) {
		int mod = n%10;
		if (mod != 0) {
			p *= mod;
		}
		n /= 10;
	}
	n = p;
	return 0;
}

int main() {
	int n;
	cin >> n;
	while (n >= 10) {
		digitProduct(n);
	}
	cout << n << endl;
}