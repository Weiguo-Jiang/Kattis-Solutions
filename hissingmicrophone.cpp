#include <iostream>
#include <string.h>

using namespace std;

int main() {
	string s;
	cin >> s;
	int flag = 0;
	for (int i = 0; i < s.length()-1; i++) {
		if (s[i] == 's' && s[i+1] == 's') {
			flag = 1;
			break;
		}
	}
	if (flag) {
		cout << "hiss" << endl;
	} else {
		cout << "no hiss" << endl;
	}
}