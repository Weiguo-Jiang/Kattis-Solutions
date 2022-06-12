#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
	unordered_map<char, int> d;
	char charList[95] = {' ', '&', ',', '2', '8', '>', 'D', 'J', 'P', 'V',
						 '\\', 'b', 'h', 'n', 't', 'z', '!', '\'', '-', '3',
						 '9', '?', 'E', 'K', 'Q', 'W', ']', 'c', 'i', 'o',
						 'u', '{', '\"', '(', '.', '4', ':', '@', 'F', 'L',
						 'R', 'X', '^', 'd', 'j', 'p', 'v', '|', '#', ')',
						 '/', '5', ';', 'A', 'G', 'M', 'S', 'Y', '_', 'e',
						 'k', 'q', 'w', '}', '$', '*', '0', '6', '<', 'B',
						 'H', 'N', 'T', 'Z', '`', 'f', 'l', 'r', 'x', '~',
						 '%', '+', '1', '7', '=', 'C', 'I', 'O', 'U', '[',
						 'a', 'g', 'm', 's', 'y'};
	int costList[95] = {0, 24, 7, 22, 23, 10, 26, 18, 23, 19, 10, 25, 21, 18,
						17, 19, 9, 3, 7, 23, 26, 15, 26, 21, 31, 26, 18, 17,
						15, 20, 17, 18, 6, 12, 4, 21, 8, 32, 20, 16, 28, 18,
						7, 25, 20, 25, 13, 12, 24, 12, 10, 27, 11, 24, 25, 28,
						25, 14, 8, 23, 21, 25, 19, 18, 29, 17, 22, 26, 10, 29,
						25, 25, 16, 22, 3, 18, 16, 13, 13, 9, 22, 13, 19, 16,
						14, 20, 18, 26, 23, 18, 23, 30, 22, 21, 24};
	for (int i = 0; i < 95; i++) {
		d[charList[i]] = costList[i];
	}
	string s;
	while (getline(cin, s)) {
		int cost = 0;
		for (int i = 0; i < s.size(); i++) {
			cost += d[s[i]];
		}
		cout << cost << endl;
	}
}