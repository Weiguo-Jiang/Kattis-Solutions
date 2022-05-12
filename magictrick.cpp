#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
	string s;
	cin >> s;
	unordered_set<char> set;
	for (auto i: s) {
		set.insert(i);
	}
	if (s.size() != set.size()) {
		cout << '0' << endl;
	} else {
		cout << '1' << endl;
	}
}