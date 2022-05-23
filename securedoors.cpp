#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
	int n;
	cin >> n;
	unordered_map<string, int> m;

	for (int i = 0; i < n; i++) {
		string e, name;
		cin >> e >> name;
		if (m.find(name) == m.end()) {
			if (e == "exit") {
				cout << name << " " << "exited (ANOMALY)" << endl;
			} else {
				cout << name << " " << "entered" << endl;
				m[name] = 1;
			}
		} else {
			if (e == "exit" && m[name] == 0) {
				cout << name << " " << "exited (ANOMALY)" << endl;
			} else if (e == "exit" && m[name] == 1) {
				cout << name << " " << "exited" << endl;
				m[name] = 0;
			} else if (e == "entry" && m[name] == 1) {
				cout << name << " " << "entered (ANOMALY)" << endl;
			} else if (e == "entry" && m[name] == 0) {
				cout << name << " " << "entered" << endl;
				m[name] = 1;
			}
		}
	}
}