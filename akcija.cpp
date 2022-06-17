#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> v;
	for (int i = 0; i < N; i++) {
		int p;
		cin >> p;
		v.push_back(p);
	}

	sort(v.begin(), v.end(), greater<int>());

	int sum = 0;
	for (int i = 0; i < N/3*3; i += 3) {
		sum += (v[i] + v[i+1]);
	}
	
	for (int i = 0; i < N%3; i++) {
		sum += v[N-1-i];
	}
	cout << sum << endl;
}