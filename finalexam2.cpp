#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<char> v1;
	vector<char> v2;
	for (int i = 0; i < n; i++) {
		char c;
		cin >> c;
		v1.push_back(c);
		if (i != 0) {
			v2.push_back(c);
		}
	}
	int cnt = 0;
	for (int i = 0; i < n-1; i++) {
		if (v1[i] == v2[i]) {
			cnt++;
		}
	}
	cout << cnt << endl;
}