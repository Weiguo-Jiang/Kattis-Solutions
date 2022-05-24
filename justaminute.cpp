#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int N;
	cin >> N;
	int Msum = 0;
	int Ssum = 0;
	int M, S;
	for (int i = 0; i < N; i++) {
		cin >> M >> S;
		Msum += M;
		Ssum += S;
	}

	double l = double(Ssum)/60/Msum;
	if (l <= 1) {
		cout << "measurement error" << endl;
		return 0;
	}
	cout << fixed << setprecision(18) << l << endl;
}