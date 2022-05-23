#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
	string s;
	cin >> s;
	unordered_map<char, int> m;
	for (int i = 0; i < s.size(); i++) {
		if (m.find(s[i]) == m.end()) {
			m[s[i]] = 1;
		} else {
			m[s[i]]++;
		}
	}

	int cnt = 0;
	for (auto i: m) {
		if (i.second % 2 == 1) {
			cnt++;
		}
	}
	if (cnt == 0) {
		cout << 0 << endl;
		return 0;
	}
	cout << cnt-1 << endl;
}