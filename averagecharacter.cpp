#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;
	getline(cin, s);
	int sum = 0;
	for (int i = 0; i < s.size(); i++) {
		sum += int(s[i]);
	}
	int avg = sum / s.size();
	cout << char(avg) << endl; 
}