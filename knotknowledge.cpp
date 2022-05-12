#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
	int n;
	cin >> n;
	unordered_set<int> set;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		set.insert(x);
	}
	for (int i = 0; i < n-1; i++) {
		int y;
		cin >> y;
		set.erase(y);
	}
	for (auto i: set) {
		cout << i << endl;
	}
}