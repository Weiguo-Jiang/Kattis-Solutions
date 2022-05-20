#include <iostream>
#include <string>

using namespace std;

int main() {
	int L, n;
	cin >> L >> n;
	int num = 0;
	int cnt = 0;

	for (int i = 0; i < n; i++) {
		string s;
		int k;
		cin >> s >> k;
		if (s == "enter") {
			if (num + k > L) {
				cnt++;
			} else {
				num += k;
			}
		} else {
			num -= k;
		}
	}
	cout << cnt << endl;
}