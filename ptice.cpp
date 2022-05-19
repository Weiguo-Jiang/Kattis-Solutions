#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	vector<char> A;
	vector<char> B;
	vector<char> C;

	for (int i = 0; i < n/3; i++) {
		A.push_back('A');
		A.push_back('B');
		A.push_back('C');
	}
	if (n%3 != 0) {
		if (n%3 == 1) {
			A.push_back('A');
		} else {
			A.push_back('A');
			A.push_back('B');
		}
	}

	for (int i = 0; i < n/4; i++) {
		B.push_back('B');
		B.push_back('A');
		B.push_back('B');
		B.push_back('C');
	}
	if (n%4 != 0) {
		if (n%4 == 1) {
			B.push_back('B');
		} else if (n%4 == 2) {
			B.push_back('B');
			B.push_back('A');
		} else {
			B.push_back('B');
			B.push_back('A');
			B.push_back('B');
		}
	}

	for (int i = 0; i < n/6; i++) {
		C.push_back('C');
		C.push_back('C');
		C.push_back('A');
		C.push_back('A');
		C.push_back('B');
		C.push_back('B');
	}
	if (n%6 != 0) {
		if (n%6 == 1) {
			C.push_back('C');
		} else if (n%6 == 2) {
			C.push_back('C');
			C.push_back('C');
		} else if (n%6 == 3) {
			C.push_back('C');
			C.push_back('C');
			C.push_back('A');
		} else if (n%6 == 4) {
			C.push_back('C');
			C.push_back('C');
			C.push_back('A');
			C.push_back('A');
		} else {
			C.push_back('C');
			C.push_back('C');
			C.push_back('A');
			C.push_back('A');
			C.push_back('B');
		}
	}

	int Adrian = 0, Bruno = 0, Goran = 0;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == A[i]) {
			Adrian++;
		}
		if (s[i] == B[i]) {
			Bruno++;
		}
		if (s[i] == C[i]) {
			Goran++;
		}
	}

	int m = max(Adrian, max(Bruno, Goran));
	cout << m << endl;
	if (Adrian == m) {
		cout << "Adrian" << endl;
	}
	if (Bruno == m) {
		cout << "Bruno" << endl;
	}
	if (Goran == m) {
		cout << "Goran" << endl;
	}
}