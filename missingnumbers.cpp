#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	
	vector<int> v;
	int t;
	cin >> t;
	if (t != 1) {
		for (int i = 1; i < t; i++) {
			v.push_back(i);
		}
	}

	int pre = t;	
	for (int i = 1; i < n; i++) {
		cin >> t;
		if (pre + 1 != t) {
			for (int j = pre+1; j < t; j++) {
				v.push_back(j);
			}
		}
		pre = t;
	}
	if (v.size() == 0) {
		cout << "good job" << endl;
	} else {
		for (int i = 0; i < v.size(); i++) {
			cout << v[i] << endl;
		}
	}
}