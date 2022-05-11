#include <iostream>
#include <string>

using namespace std;

int main() {
	int ans = 1;
	string p1, p2;
	cin >> p1 >> p2;
	for (int i = 0; i < 4; i++) {
		if (p1[i] != p2[i]) {
			ans *= 2;
		}
	}
	cout << ans << endl;
}