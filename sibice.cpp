#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int N;
	int W, H;
	cin >> N >> W >> H;
	double l = sqrt(W*W + H*H);
	for (int i = 0; i < N; i++) {
		int m;
		cin >> m;
		if (m > l) {
			cout << "NE" << endl;
		} else {
			cout << "DA" << endl;
		}
	}
}