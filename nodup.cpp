#include <iostream>
#include <unordered_set>
#include <sstream>

using namespace std;

int main() {
	unordered_set<string> set;
	int cnt = 0;
	string str, s;
	getline(cin, str);
	stringstream ss(str);
	while (ss >> s) {
		cnt++;
		set.insert(s);
	}
	if (cnt == set.size()) {
		cout << "yes" << endl;
	} else {
		cout << "no" << endl;
	}
}