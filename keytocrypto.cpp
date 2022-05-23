#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string ciphertext, key;
	cin >> ciphertext >> key;
	vector<char> v;
	
	for (int i = 0; i < key.size(); i++) {
		v.push_back(key[i]);
	}

	int cnt = 0;

	vector<char> deciphered;

	for (int i = 0; i < ciphertext.size(); i++) {
		if (ciphertext[i] >= v[cnt]) {
			char c = char(ciphertext[i]-v[cnt]+'A');
			deciphered.push_back(c);
			v.push_back(c);
		} else {
			char c = char(ciphertext[i]-v[cnt]+'A'+26);
			deciphered.push_back(c);
			v.push_back(c);
		}
		cnt++;
	}

	for (int i = 0; i < ciphertext.size()-1; i++) {
		cout << deciphered[i];
	}
	cout << deciphered[ciphertext.size()-1] << endl;
}
