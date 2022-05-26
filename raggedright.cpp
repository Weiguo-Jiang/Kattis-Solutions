#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	string s;
	vector<int> lens;
	int max = -1;
	while (getline(cin, s)) {
		int len = s.size();
		lens.push_back(len);
		if (len > max) {
			max = len;
		}
	}

	int raggedness = 0;
	for (int i = 0; i < lens.size()-1; i++) {
		raggedness += (lens[i]-max)*(lens[i]-max);
	}

	cout << raggedness << endl;
}