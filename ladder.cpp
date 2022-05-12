#include <iostream>
#include <cmath>

using namespace std;

#define PI 3.1415926

int main() {
	int h, v;
	cin >> h >> v;
	int l = ceil(h/sin(v*PI/180.0));
	cout << l << endl;
}