#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
	unordered_map<char, int> dict;
	string s;
	cin >> s;
	for (auto i: s) {
		if (dict.find(i) == dict.end()) {
			dict[i] = 1;
		} else {
			dict[i] += 1;
		}
	}
	int flag = 0;
	if (dict.find('T') != dict.end() &&
		dict.find('C') != dict.end() &&
		dict.find('G') != dict.end()) {
		flag = min(min(dict['T'], dict['C']), dict['G']);
	}
	int ans = flag*7;
	for (auto it = dict.begin(); it != dict.end(); it++) {
		ans += it->second * it->second;
	}
	cout << ans << endl;
}