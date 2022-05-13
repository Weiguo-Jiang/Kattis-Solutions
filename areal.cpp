#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {
	long long int area;
	cin >> area;
	double length = sqrt(area)*4;
	cout << fixed << setprecision(10) << length << endl;
}