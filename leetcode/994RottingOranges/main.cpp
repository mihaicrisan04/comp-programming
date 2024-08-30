#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int n, m;
    vector<int> di = {-1, 0, 1, 0};
    vector<int> dj = {0, 1, 0, -1};

    bool inMat(int i, int j) { return i >= 0 && i < n && j >= 0 && j < m; }

    void fill(int i, int j, int k, vector<vector<int>>& grid) {
        grid[i][j] = k;
        for (int d = 0; d < 4; d++) {
            int ii = i + di[d];
            int jj = j + dj[d];
            if (inMat(ii, jj) && (grid[ii][jj] == 1 || grid[ii][jj] < k)) {
                fill(ii, jj, k-1, grid);
            }
        }
    }


    int orangesRotting(vector<vector<int>>& grid) {
        n = grid.size();        
        m = grid[0].size();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    fill(i, j, 0, grid);
                }
            }
        }

        int maxTime = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) return -1;
                maxTime = min(maxTime, grid[i][j]);
            }
        }
        return -maxTime;
    }
};


int main() {
    Solution s;
    vector<vector<int>> grid = {{2,1,1},{1,1,0},{0,1,1}};
    cout << s.orangesRotting(grid) << endl;
    vector<vector<int>> grid2 = {{2,1,1},{0,1,1},{1,0,1}};
    cout << s.orangesRotting(grid2) << endl;
    vector<vector<int>> grid3 = {{0,2}};
    cout << s.orangesRotting(grid3) << endl;
    return 0;
}