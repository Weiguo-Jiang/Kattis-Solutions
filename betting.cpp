#include <iostream>

using namespace std;

int main() {
    double a;
    cin >> a;
    double r1 = 1/a * 100.0;
    double r2 = 1/(100.0-a) * 100.0;
    cout << r1 << endl;
    cout << r2 << endl;
}