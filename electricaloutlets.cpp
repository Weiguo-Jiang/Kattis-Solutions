#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int K;
		cin >> K;
		int sum = 0;
		for (int j = 0; j < K; j++) {
			int o;
			cin >> o;
			sum += o;
		}
		cout << sum-K+1 << endl;
	}
}