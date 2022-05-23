#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;
	int space = 0;
	int cnt = 0;
	while (cin >> s) {
		space++;
		for (int i = 0; i < s.size()-1; i++) {
			if (s[i] == 'a' && s[i+1] == 'e') {
				cnt++;
				break;
			}
		}
	}
	double p = double(cnt) / space;
	if (p >= 0.4) {
		cout << "dae ae ju traeligt va" << endl;
	} else {
		cout << "haer talar vi rikssvenska" << endl;
	}
}