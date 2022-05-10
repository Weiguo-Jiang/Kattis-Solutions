#include <iostream>

using namespace std;

int main() {
	int X, N, ans;
	cin >> X >> N;
	ans = X*N+X;
	for (int i = 0; i < N; i++) {
		int used;
		cin >> used;
		ans -= used;
	}
	cout << ans << endl;
}