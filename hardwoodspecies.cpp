#include <iostream>
#include <map>
#include <string>
#include <iomanip>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string s;
	int cnt = 0;
	map<string, int> m;
	while (getline(cin, s)) {
		m[s]++;
		cnt++;
	}

	for (auto i = m.begin(); i != m.end(); i++) {
		cout << i->first << " ";
		cout << fixed << setprecision(10) << i->second*1.0/cnt*100.0 << endl;
	}
}