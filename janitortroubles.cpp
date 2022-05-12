#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {
	int a, b, c, d;
	cin >> a >> b >> c >> d;
	double semi = (a+b+c+d)/2.0;
	double ans = sqrt((semi-a)*(semi-b)*(semi-c)*(semi-d));
	cout << fixed << setprecision(10) << ans << endl;
}