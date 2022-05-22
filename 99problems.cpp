#include <iostream>

using namespace std;

int endIn99(int n) {
	if (n % 100 == 99) {
		return 1;
	} else {
		return 0;
	}
}

int main() {
	int N;
	cin >> N;

	int n = N;

	int max = 0, min = 0;
	while (true) {
		n += 1;
		if (endIn99(n)) {
			max = n;
			break;
		}
	}

	n = N;

	while (true && n > 0) {
		n -= 1;
		if (endIn99(n)) {
			min = n;
			break;
		}
	}

	if (max - N > N - min && endIn99(min)) {
		cout << min << endl;
	} else {
		cout << max << endl;
	}
}