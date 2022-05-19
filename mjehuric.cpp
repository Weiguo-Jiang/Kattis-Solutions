#include <iostream>

using namespace std;

int print(int* arr) {
	for (int i = 0; i < 4; i++) {
		cout << arr[i] << " ";
	}
	cout << arr[4] << endl;
	
	int flag = 1;
	for (int i = 0; i < 4; i++) {
		if (arr[i] > arr[i+1]) {
			flag = 0;
		}
	}
	return flag;
}

int main() {
	int arr[5];
	cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4];
	
	while (true) {
		if (arr[0] > arr[1]) {
			int c = arr[0];
			arr[0] = arr[1];
			arr[1] = c;
			int flag = print(arr);
			if (flag) {
				break;
			}
		}

		if (arr[1] > arr[2]) {
			int c = arr[1];
			arr[1] = arr[2];
			arr[2] = c;
			int flag = print(arr);
			if (flag) {
				break;
			}
		}

		if (arr[2] > arr[3]) {
			int c = arr[2];
			arr[2] = arr[3];
			arr[3] = c;
			int flag = print(arr);
			if (flag) {
				break;
			}
		}

		if (arr[3] > arr[4]) {
			int c = arr[3];
			arr[3] = arr[4];
			arr[4] = c;
			int flag = print(arr);
			if (flag) {
				break;
			}
		}
	}
}