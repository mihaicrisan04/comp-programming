#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        int arrows = 1;
        int start = points[0][0], end = points[0][1];

        for (int p = 1; p < points.size(); p++) {
            if (points[p][0] > end) {
                arrows += 1;
            }
        } 

        return arrows;
    }
};


int main() {
    Solution s;
    vector<vector<int>> points = {{10, 16}, {2, 8}, {1, 6}, {7, 12}};
    cout << s.findMinArrowShots(points) << endl; // 2
    vector<vector<int>> points2 = {{1, 2}, {3, 4}, {5, 6}, {7, 8}};
    cout << s.findMinArrowShots(points2) << endl; // 4
    vector<vector<int>> points3 = {{1, 2}, {2, 3}, {3, 4}, {4, 5}};
    cout << s.findMinArrowShots(points3) << endl; // 2
    vector<vector<int>> points4 = {{1, 2}};
    cout << s.findMinArrowShots(points4) << endl; // 1
    vector<vector<int>> points5 = {{2, 3}, {2, 3}};
    cout << s.findMinArrowShots(points5) << endl; // 1
    return 0;
}