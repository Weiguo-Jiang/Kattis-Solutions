#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int c;
		cin >> c;

		int mod = c % 400;
		if (mod != 0) {
			cout << c / 400 + 1 << endl;
		} else {
			cout << c / 400 << endl;
		}
	}
}