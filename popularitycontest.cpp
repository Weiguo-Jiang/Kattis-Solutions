#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> v;
	for (int i = 1; i <= N; i++) {
		v.push_back(i);
	}

	int M;
	cin >> M;
	int a, b;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		v[a-1]--;
		v[b-1]--;
	}

	for (int i = 0; i < N-1; i++) {
		cout << -v[i] << " ";
	}
	cout << -v[N-1] << endl;
}