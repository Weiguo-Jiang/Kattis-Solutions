#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	double C, L;
	cin >> C >> L;
	double cost = 0;
	for (int i = 0; i < L; i++) {
		double a, b;
		cin >> a >> b;
		cost += a*b*C;
	}
	cout << fixed << setprecision(10) << cost << endl;
}