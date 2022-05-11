#include <iostream>

using namespace std;

int main() {
	int H, M;
	cin >> H >> M;
	if (H == 0) {
		H = 24;
	}
	int t = H*60+M;
	t -= 45;
	H = t / 60;
	M = t % 60;
	cout << H << " " << M << endl;
}