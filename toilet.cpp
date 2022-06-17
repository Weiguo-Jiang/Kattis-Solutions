#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;
	cin >> s;
	int len = s.size();

	char status = s[0];
	int cnt1 = 0;
	for (int i = 1; i < len; i++) {
		if (s[i] != status) {
			cnt1++;
			status = s[i];
		}
		if (status != 'U') {
			cnt1++;
			status = 'U';
		}
	}
	cout << cnt1 << endl;

	status = s[0];
	int cnt2 = 0;
	for (int i = 1; i < len; i++) {
		if (s[i] != status) {
			cnt2++;
			status = s[i];
		}
		if (status != 'D') {
			cnt2++;
			status = 'D';
		}
	}
	cout << cnt2 << endl;

	status = s[0];
	int cnt3 = 0;
	for (int i =1; i < len; i++) {
		if (s[i] != status) {
			cnt3++;
			status = s[i];
		}
	}
	cout << cnt3 << endl;
}