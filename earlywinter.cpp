#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, dm;
	cin >> n >> dm;
	int cnt = 0;
	int ans = 0;
	int flag = 1;
	for (int i = 0; i < n; i++) {
		int d;
		cin >> d;
		if (d > dm) {
			cnt++;
		}
		if (d <= dm and flag) {
			flag = 0;
			ans = cnt;
		}
	}
	if (cnt == n) {
		cout << "It had never snowed this early!" << endl;
	} else {
		cout << "It hadn't snowed this early in " << ans << " years!" << endl;
	}
}