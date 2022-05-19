#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int g;
		cin >> g;
		int k = -1;
		int flag = 1;
		for (int j = 0; j < g; j++) {
			int c = k;
			cin >> k;
			if (k != c+1 && j != 0 && j != g-1 && flag) {
				cout << j+1 << endl;
				flag = 0;
			}
		}
	}
}