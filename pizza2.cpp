#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int R, C;
	cin >> R >> C;
	cout << fixed << setprecision(8) << (R-C)*(R-C)/double(R)/R*100.0 << endl;
}