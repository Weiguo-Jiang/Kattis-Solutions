#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int n;
		cin >> n;
		int d = 1;
		for (int j = 1; j < n+1; j++) {
			d *= j;
			d %= 10;
		}
		cout << d << endl;
	}
}