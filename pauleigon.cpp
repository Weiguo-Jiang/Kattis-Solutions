#include <iostream>

using namespace std;

int main() {
	int N, P, Q;
	cin >> N >> P >> Q;

	int div = (P+Q)/N;

	if ((div+1)%2 == 1) {
		cout << "paul" << endl;
		} else {
		cout << "opponent" << endl;
	}
}