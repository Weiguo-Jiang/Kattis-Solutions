#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m;
	while (true) {
		vector<int> v1, v2, ans;
		cin >> n >> m;
		if (n == 0 and m == 0) {
			break;
		}

		int cd;
		for (int i = 0; i < n; i++) {
			cin >> cd;
			v1.push_back(cd);
		}

		for (int i = 0; i < m; i++) {
			cin >> cd;
			v2.push_back(cd);
		}

		set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), back_inserter(ans));
		cout << ans.size() << endl;
	}
}