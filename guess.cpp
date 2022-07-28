#include <iostream>
#include <string>

using namespace std;

int main() {
	int lower = 1;
	int upper = 1000;
	int guess = -1;
	string op = "";
	while (op != "correct") {
		guess = (lower+upper)/2;
		cout << guess << endl;
		cout << flush;
		cin >> op;

		if (op == "lower") {
			upper = guess-1;
		} else if (op == "higher") {
			lower = guess+1;
		}
	}
}