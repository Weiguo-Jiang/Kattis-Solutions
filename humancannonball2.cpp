#include <iostream>
#include <string>
#include <math.h>

#define PI 3.14159265

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		double v, theta, x, h1, h2;
		cin >> v >> theta >> x >> h1 >> h2;
		double t = x/v/cos(theta*PI/180.0);
		double y = v*t*sin(theta*PI/180.0)-0.5*9.81*t*t;
		if (y + 1 <= h2 && y - 1 >= h1) {
			cout << "Safe" << endl;
		} else {
			cout << "Not Safe" << endl;
		}
	}
}