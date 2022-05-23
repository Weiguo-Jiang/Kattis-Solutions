#include <iostream>

using namespace std;

int main() {
	int A, B, C, I, J, K;
	cin >> A >> B >> C >> I >> J >> K;
	double a = double(A) / I;
	double b = double(B) / J;
	double c = double(C) / K;

	if (a <= b && a <= c) {
		cout << 0 << " " << B - a*J << " " << C - a*K << endl;
	} else if (b <= a && b <= c) {
		cout << A - b*I << " " << 0 << " " << C - b*K << endl;
	} else {
		cout << A - c*I << " " << B - c*J << " " << 0 << endl;
	}
}