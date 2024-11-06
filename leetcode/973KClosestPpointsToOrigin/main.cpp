#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    struct Point {
        double d;
        int x, y;

        bool operator<(const Point& p) const {
            return d < p.d;
        }
    };
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<Point> pq;

        for (auto p : points) {
            pq.push({-sqrt(p[0] * p[0] + p[1] * p[1]), p[0], p[1]});
        }   

        vector<vector<int>> res;
        while (k--) {
            Point p = pq.top();
            res.push_back({p.x, p.y});
            pq.pop();
        }

        return res;
    }
};


int main() {
    Solution s;
    vector<vector<int>> points = {{1, 3}, {-2, 2}};
    int k = 1;
    vector<vector<int>> res = s.kClosest(points, k);
    for (auto p : res) {
        cout << p[0] << " " << p[1] << endl;
    }
    return 0;
}