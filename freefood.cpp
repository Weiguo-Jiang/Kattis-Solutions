#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
	int n;
	cin >> n;
	unordered_set<int> set;
	for (int i = 0; i < n; i++) {
		int s, t;
		cin >> s >> t;
		for (int j = s; j <= t; j++) {
			set.insert(j);
		}
	}
	cout << set.size() << endl;
}