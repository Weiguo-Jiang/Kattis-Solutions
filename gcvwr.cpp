#include <iostream>

using namespace std;

int main() {
	int G, T, N;
	cin >> G >> T >> N;
	double ans = double(G-T) * 0.9;
	for (int i = 0; i < N; i++) {
		int w;
		cin >> w;
		ans -= w;
	}
	cout << ans << endl;
}