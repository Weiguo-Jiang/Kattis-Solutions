#include <iostream>

using namespace std;

int main() {
	double a, b, c, d;
	cin >> a >> b >> c >> d;
	double area = (c-a)*(d-b);
	if (area < 0) {
		cout << -1 * area << endl;
	} else {
		cout << area << endl;
	}
}