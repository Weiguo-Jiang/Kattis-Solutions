#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	unordered_map<int, int> dict;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			int sum = i + j;
			if (dict.find(sum) == dict.end()) {
				dict[sum] = 1;
			} else {
				dict[sum] += 1;
			}
		}
	}
	int max = 0;
	for (auto it = dict.begin(); it != dict.end(); it++) {
		if (it->second > max) {
			max = it->second;
		}
	}
	vector<int> ans;
	for (auto it = dict.begin(); it != dict.end(); it++) {
		if (it->second == max) {
			ans.push_back(it->first);
		}
	}
	sort(ans.begin(), ans.end());
	for (auto it = ans.begin(); it != ans.end(); it++) {
		cout << *it << endl;
	}
}