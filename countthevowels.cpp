#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	string s;
	getline(cin, s);
	int cnt = 0;
	transform(s.begin(), s.end(), s.begin(), ::tolower);
	for (auto i: s) {
		if (i == 'a' || i == 'e' || i == 'i'
			|| i == 'o' || i == 'u') {
			cnt++;
		}
	}
	cout << cnt << endl;
}