#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int N;
	cin >> N;
	int sum = 0;
	for (int i = 0; i < N; i++) {
		int P;
		cin >> P;
		int p = P % 10;
		int n = P / 10;
		sum += pow(n, p);
	}
	cout << sum << endl;
}