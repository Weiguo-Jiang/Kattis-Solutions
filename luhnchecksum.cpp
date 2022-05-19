#include <iostream>
#include <string>

using namespace std;

int digitSum(int n) {
	int sum = 0;
	while (n != 0) {
		sum += (n % 10);
		n /= 10;
	}
	return sum;
}

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int sum = 0;
		string s;
		cin >> s;
		for (int j = s.size()-2; j >= 0; j -= 2) {
			sum += digitSum((int(s[j])-48)*2);
		}

		for (int j = s.size()-1; j >= 0; j -= 2) {
			sum += (int(s[j])-48);
		}

		if (sum % 10 == 0) {
			cout << "PASS" << endl;
		} else {
			cout << "FAIL" << endl;
		}
	}
}