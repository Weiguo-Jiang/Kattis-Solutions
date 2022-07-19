#include <iostream>
#include <string>

using namespace std;

int reduced(int n, int d, int i) {
	if (d%n == 0) {
		d /= n;
		if (d >= i) {
			return 1;
		}
	}
	return 0;
}

int main() {
	ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
	string s;
	while(cin >> s) {
		int index = 0;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '/') {
				index++;
				break;
				}
			index++;
		}
		
		int d = stoi(s.substr(index, s.size()-index));

		int cnt = 0;
		for (int i = d+1; i <= 2*d; i++) {
			int n = i-d;
			int d2 = d*i;
			cnt += reduced(n, d2, i);
		}
		cout << cnt << endl;
	}
}