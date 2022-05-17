#include <iostream>

using namespace std;

int digitSum(int N) {
	int sum = 0;
	while (N != 0) {
		sum += N%10;
		N /= 10;
	}
	return sum;
}

int main() {
	int N;
	while (true) {
		cin >> N;
		if (N == 0) {
			break;
		}
		int s = digitSum(N);
		
		int p = 11;
		for (int i = p; i <= 100; i++) {
			int s1 = digitSum(i*N);
			if (s1 == s) {
				cout << i << endl;
				break;
			}
		}
	}
}
