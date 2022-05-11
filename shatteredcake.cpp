#include <iostream>

using namespace std;

int main() {
	int W, N;
	cin >> W >> N;
	int area = 0;
	for (int i = 0; i < N; i++) {
		int l, w;
		cin >> l >> w;
		area += l*w;
	}
	cout << area/W << endl;
}