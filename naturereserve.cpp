//
// BEGIN-HEADER
//
// Name: Weiguo Jiang
//
// Student-ID: 1670913
//
// List any resources you used below (eg. urls, name of the algorithm from our code archive).
// Remember, you are permitted to get help with general concepts about algorithms
// and problem-solving, but you are not permitted to hunt down solutions to
// these particular problems!
//
// KACTL Repo: https://github.com/kth-competitive-programming/kactl
//
// By submitting this code, you are agreeing that you have solved in accordance
// with the collaboration policy in CMPUT 303/403.
//
// END-HEADER
//

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    for (int _ = 0; _ < n; ++_) {
        int N, M, L, S;
        cin >> N >> M >> L >> S;
        vector<bool> visited(N, false);
        vector<int> initial_stations;
        for (int __ = 0; __ < S; ++__) {
            int init;
            cin >> init;
            visited[init-1] = true;
            initial_stations.push_back(init-1);
        }
        unordered_map<int, vector<pair<int, int>>> adj;
        for (int __ = 0; __ < N; ++__) {
            adj[__] = {};
        }
        for (int __ = 0; __ < M; ++__) {
            int i, j, E;
            cin >> i >> j >> E;
            --i;
            --j;
            adj[i].push_back(make_pair(E+L, j));
            adj[j].push_back(make_pair(E+L, i));
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        for (int i : initial_stations) {
            for (auto value : adj[i]) {
                heap.push(value);
            }
        }
        long long energy = 0;
        while (!heap.empty()) {
            int e = heap.top().first;
            int node = heap.top().second;
            heap.pop();
            if (!visited[node]) {
                visited[node] = true;
                energy += e;
                for (auto value : adj[node]) {
                    heap.push(value);
                }
            }
        }
        cout << energy << endl;
    }
    return 0;
}