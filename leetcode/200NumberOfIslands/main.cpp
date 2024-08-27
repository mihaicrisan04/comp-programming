#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int n, m;
    int k = 0;
    vector<int> di = {-1, 0, 1, 0};
    vector<int> dj = {0, 1, 0, -1};

    bool inMat(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    void fill(int i, int j, vector<vector<char>>& grid) {   
        grid[i][j] = '0';
        for (int d = 0; d < 4; d++) {
            int ii = i + di[d];
            int jj = j + dj[d];
            if (inMat(ii, jj) && grid[ii][jj] == '1') {
                fill(ii, jj, grid);
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        n = grid.size();        
        m = grid[0].size();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    fill(i, j, grid);
                    k++;
                }
            }
        }

        return k;
    }
};


int main() {
    Solution s;
    vector<vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}
    };
    cout << s.numIslands(grid) << endl;
    return 0;
}