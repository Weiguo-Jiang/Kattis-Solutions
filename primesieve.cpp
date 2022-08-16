#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, q;
	cin >> n >> q;

	vector<bool> v(n+1, true);
	v[0] = false;
	v[1] = false;

	int cnt = 0;
	int root = 2;
	while (root*root <= n) {
		if (v[root]) {
			cnt++;
			for (int j = root*root; j <= n; j += root) {
				v[j] = false;
			}
		}
		root++;
	}

	for (int i = root; i <= n; i++) {
		if(v[i]) {
			cnt++;
		}
	}
	cout << cnt << endl;

	for (int i = 0; i < q; i++) {
		int num;
		cin >> num;
		cout << v[num] << endl;
	}
}