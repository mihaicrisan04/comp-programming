#include <bits/stdc++.h>    

using namespace std;


class Solution {
public:
    int n;
    vector<int> r, t;

    int root(int node) {
        if (t[node] == -1) return node;
        return root(t[node]);
    }

    void unite(int ra, int rb) {
        if (r[ra] < r[rb]) { t[ra] = rb; }
        else {
            t[rb] = ra;
            if (r[ra] == r[rb]) r[ra]++; 
        }
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        n = edges.size();
        t = vector<int>(n+1, -1);
        r = vector<int>(n+1, 0);

        int solIdx = -1;
        for (int i = 0; i < n; i++) {
            int ra = root(edges[i][0]);
            int rb = root(edges[i][1]);
            if (ra != rb) { unite(ra, rb); }
            else { solIdx = i; break;}
        }
        return edges[solIdx];
    }
};


int main() {
    Solution s;

    vector<vector<int>> edges = {{1, 2}, {1, 3}, {2, 3}};
    vector<int> res = s.findRedundantConnection(edges);
    cout << res[0] << " " << res[1] << endl;

    vector<vector<int>> edges2 = {{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}};
    vector<int> res2 = s.findRedundantConnection(edges2);
    cout << res2[0] << " " << res2[1] << endl;

    return 0;
}