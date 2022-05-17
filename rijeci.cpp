#include <iostream>

using namespace std;

int main() {
	int A, B, K;
	cin >> K;
	A = 1;
	B = 0;
	for (int i = 0; i < K; i++) {
		int C = A;
		A += B;
		B += C;
		A -= C;
	}
	cout << A << " " << B << endl;
}