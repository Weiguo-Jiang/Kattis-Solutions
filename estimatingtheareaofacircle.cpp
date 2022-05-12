#include <iostream>
#include <iomanip>

using namespace std;

#define PI 3.141592654

int main() {
	double r, m, c;
	while (true){
		cin >> r >> m >> c;
		if (r == 0 && m == 0 && c == 0){
			return 0;
		}
		double area = PI * r * r;
		double estimate = c/m*r*r*4;
		cout << fixed << setprecision(10) << area << " " << estimate << endl;
	}
}