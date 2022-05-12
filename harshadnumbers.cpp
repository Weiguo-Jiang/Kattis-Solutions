#include <iostream>

using namespace std;

int digitsum(int n) {
	int digitsum = 0;
	while (n != 0) {
		digitsum += n%10;
		n /= 10;
	}
	return digitsum;
}

int main() {
	int n;
	cin >> n;
	while (true){
		if (n%digitsum(n) == 0) {
			cout << n << endl;
			break;
		} else {
			n++;
		}
	}
}