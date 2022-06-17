#include <iostream>

using namespace std;

int main() {
	int h, w, n;
	cin >> h >> w >> n;
	int currWidth = 0, cnt = 0, flag = 0;
	for (int i = 0; i < n; i++) {
		int brick;
		cin >> brick;
		currWidth += brick;
		if (currWidth == w) {
			currWidth = 0;
			cnt++;
		} else if (currWidth > w) {
			flag = 1;
			break;
		}
	}
	if (flag) {
		cout << "NO" << endl;
	} else {
		if (cnt >= h) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
}