#include <iostream>

using namespace std;

int main() {
	int a, b, c, d, e, s;
	cin >> a >> b >> c >> d >> e >> s;
	if (s >= a) {
		cout << 'A' << endl;
	} else if (s >= b) {
		cout << 'B' << endl;
	} else if (s >= c) {
		cout << 'C' << endl;
	} else if (s >= d) {
		cout << 'D' << endl;
	} else if (s >= e) {
		cout << 'E' << endl;
	} else {
		cout << 'F' << endl;
	}
}