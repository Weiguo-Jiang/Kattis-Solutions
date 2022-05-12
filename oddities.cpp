#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int N;
		cin >> N;
		if (N%2 != 0) {
			cout << N << " is odd" << endl;
		} else {
			cout << N << " is even" << endl;
		}
	}
}