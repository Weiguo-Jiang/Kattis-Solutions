#include <iostream>
#include <string>

using namespace std;

int main() {
	string s1, s2;
	cin >> s1 >> s2;
	int index1, index2;

	int flag = 0;
	for (int i = 0; i < s1.size(); i++) {
		for (int j = 0; j < s2.size(); j++) {
			if (s1[i] == s2[j]) {
				index1 = i;
				index2 = j;
				flag = 1;
				break;
			}
		}
		if (flag) {
			break;
		}
	}

	for (int i = 0; i < s2.size(); i++) {
		for (int j = 0; j < s1.size(); j++) {
			if (i != index2 && j != index1) {
				cout << ".";
			} else if (i == index2) {
				cout << s1[j];
			} else {
				cout << s2[i];
			}
		}
		cout << endl;
	}
}