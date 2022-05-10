#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	int L = 0;
	for (int i = 0; i < N; i++) {
		int l;
		cin >> l;
		L += l;
	}
	cout << L-N+1 << endl;
}