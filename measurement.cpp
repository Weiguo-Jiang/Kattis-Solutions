#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
	unordered_map<string, int> d;
	d["thou"] = 1;
	d["th"] = 1;
	d["inch"] = 1000;
	d["in"] = 1000;
	d["foot"] = 1000 * 12;
	d["ft"] = 1000 * 12;
	d["yard"] = 1000 * 12 * 3;
	d["yd"] = 1000 * 12 * 3;
	d["chain"] = 1000 * 12 * 3 * 22;
	d["ch"] = 1000 * 12 * 3 * 22;
	d["furlong"] = 1000 * 12 * 3 * 22 *10;
	d["fur"] = 1000 * 12 * 3 * 22 *10;
	d["mile"] = 1000 * 12 * 3 * 22 *10 * 8;
	d["mi"] = 1000 * 12 * 3 * 22 *10 * 8;
	d["league"] = 1000 * 12 * 3 * 22 *10 * 8 * 3;
	d["lea"] = 1000 * 12 * 3 * 22 *10 * 8 * 3;

	double n;
	string s1, s2, s3;
	cin >> n >> s1 >> s2 >> s3;
	double op = n * d[s1] / d[s3];
	cout << fixed << setprecision(10) << op << endl;
}