#include <iostream>

using namespace std;

int main() {
	int wc, hc, ws, hs;
	cin >> wc >> hc >> ws >> hs;
	if (ws + 2 <= wc && hs + 2 <= hc) {
		cout << "1" << endl;
	} else {
		cout << "0" << endl;
	}
}