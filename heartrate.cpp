#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		double b, p;
		cin >> b >> p;
		double BPM = b*60/p;
		double minABPM = 60/(p/(b-1));
		double maxABPM = 60/(p/(b+1));
		cout << minABPM << " " << BPM << " " << maxABPM << endl;
	}
}