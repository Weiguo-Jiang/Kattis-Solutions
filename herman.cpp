#include <iostream>
#include <iomanip>

using namespace std;

#define pi 3.14159265358979323846

int main() {
	int R;
	cin >> R;
	double Euclidian = R * R * pi;
	double taxicab = R * R * 2;
	cout << fixed << setprecision(6) << Euclidian << endl;
	cout << fixed << setprecision(6) << taxicab << endl;
}