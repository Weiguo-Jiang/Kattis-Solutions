#include <iostream>

using namespace std;

int main() {
	int a, b;
	while (true) {
		cin >> a >> b;
		if (a == 0 && b == 0) {
			break;
		}
		int m = a / b;
		int n = a % b;
		cout << m << " " << n << " / " << b << endl;
	}
}