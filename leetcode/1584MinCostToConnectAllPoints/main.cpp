#include <bits/stdc++.h>

using namespace std;

class Solution {
public:

    struct Edge {
        int a, b, c;

        bool operator<(const Edge& other) const {
            return c < other.c;
        }

        Edge(int a, int b, int c) : a(a), b(b), c(c) {}
    };


    vector<int> r, t;
    vector<Edge> edges;
    
    int minCostConnectPoints(vector<vector<int>>& points) {
        r = vector<int>(points.size() + 1, 0);
        t = vector<int>(points.size() + 1, -1);

        for (int i = 0; i < points.size() - 1; i++) {
            for (int j = i + 1; j < points.size(); j++) {
                int x1 = points[i][0];
                int y1 = points[i][1];
                int x2 = points[j][0];
                int y2 = points[j][1];

                int d = abs(x1 - x2) + abs(y1 - y2);
                edges.push_back({i, j, d});
            }
        }

        int apmCost = 0;
        sort(edges.begin(), edges.end());

        for (auto e : edges) {
            int ra = root(e.a);
            int rb = root(e.b);
            if (ra != rb) {
                unite(ra, rb);
                apmCost += e.c;
                cout << ra << ' ' << rb << ' ' << e.c << '\n';
            }
        }

        for (auto i : r) {
            cout << i << ' ';
        }
        cout << '\n';
        for (auto i : t) {
            cout << i << ' ';
        }

        return apmCost;
    }

    int root(int node) {
        if (t[node] == -1) return node;
        return root(t[node]);
    }

    void unite(int ra, int rb) {
        if (r[ra] < r[rb]) {
            t[ra] = rb;
        }
        else {
            t[rb] = ra;
            if (r[ra] == r[rb]) {
                r[ra]++;
            }
        }
    }
};


int main() {
    Solution s;
    vector<vector<int>> points = {{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}};
    cout << s.minCostConnectPoints(points);
    return 0;
}