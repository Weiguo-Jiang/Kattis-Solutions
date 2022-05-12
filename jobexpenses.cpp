#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	int sum = 0;
	for (int i = 0; i < N; i++) {
		int n;
		cin >> n;
		if (n < 0) {
			sum += n;
		}
	}
	cout << 0-sum << endl;
}