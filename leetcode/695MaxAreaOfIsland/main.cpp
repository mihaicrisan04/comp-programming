#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSize = 0;
    int n, m;
    vector<int> di = {-1, 0, 1, 0};
    vector<int> dj = {0, 1, 0, -1};

    bool inMat(int i, int j) { return i >= 0 && i < n && j >= 0 && j < m; }

    void fill(int i, int j, vector<vector<int>>& grid, int& size) {
        size++;
        grid[i][j] = 0;
        for (int d = 0; d < 4; d++) {
            int ii = i + di[d];
            int jj = j + dj[d];
            if (inMat(ii, jj) && grid[ii][jj] == 1) {
                fill(ii, jj, grid, size);
            }
        }
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();        

        int size;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    size = 0;
                    fill(i, j, grid, size);
                    maxSize = max(maxSize, size);
                }
            }
        }
        
        return maxSize;
    }
};


int main() {
    Solution s;

    return 0;
}