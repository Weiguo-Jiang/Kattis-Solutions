#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	int cnt = 0;
	int m = 0;
	for (int i = 0; i < N; i++) {
		int n;
		cin >> n;
		if (n > m) {
			cnt++;
		}
		m = n;
	}
	cout << cnt << endl;
}