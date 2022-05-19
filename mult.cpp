#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int flag = 1;
	int initial;
	for (int i = 0; i < n; i++) {
		if (flag) {
			cin >> initial;
			flag = 0;
			continue;
		}
		int k;
		cin >> k;
		if (k % initial == 0) {
			cout << k << endl;
			flag = 1;
		}
	}
}