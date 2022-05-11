#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	if (N % 2 == 1) {
		cout << "still running" << endl;
		return 0;
	}
	int flag = 0;
	int time = 0;
	vector<int> v;
	for (int i = 0; i < N; i++) {
		int t;
		cin >> t;
		v.push_back(t);
		if (flag == 0) {
			flag = 1;
		} else {
			flag = 0;
		}
	}
	for (int i = 1; i < N; i += 2) {
		time += (v[i]-v[i-1]);
	}
	cout << time << endl;
}