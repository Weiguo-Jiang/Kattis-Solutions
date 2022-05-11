#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int ans = 0;
		int n;
		cin >> n;
		int m = n;
		while (n != 0) {
			cin >> n;
			if (n > m*2) {
				ans += (n-2*m);
			}
			m = n;
		}
		cout << ans << endl;
	}
}