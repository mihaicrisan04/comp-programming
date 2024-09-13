#include <bits/stdc++.h>

using namespace std;


// ## Work In Progress
class Solution {
public:
    int n, m;
    vector<int> di = {-1, 0, 1, 0};
    vector<int> dj = {0, 1, 0, -1};
    int minCost = 1e9;
    vector<vector<int>> viz;


    bool inMat(int i, int j) {
        return i >= 0 && i < n && j >= 0 && j < m;
    }

    void dfs(int i, int j, int currCost, vector<vector<int>>& grid) {
        if (i == n - 1 && j == m - 1) {
            minCost = min(minCost, currCost);
            return;
        }

        viz[i][j] = 1;
        for (int d = 0; d < 4; d++) {
            int ii = i + di[d];
            int jj = j + dj[d];
            if (inMat(ii, jj) && !viz[ii][jj]) {
                dfs(ii, jj, (currCost < grid[ii][jj] ? grid[ii][jj] - currCost : 0), grid);
            }
        }
        viz[i][j] = 0;
    }

    int swimInWater(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        viz = vector<vector<int>>(n, vector<int>(m, 0));

        dfs(0, 0, 0, grid);

        return minCost;
    }    
};


int main() {
    Solution s; 
    vector<vector<int>> grid = {{0,2},{1,3}};
    cout << s.swimInWater(grid) << endl;
    vector<vector<int>> grid2 = {{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}};
    cout << s.swimInWater(grid2) << endl;
    return 0;
}