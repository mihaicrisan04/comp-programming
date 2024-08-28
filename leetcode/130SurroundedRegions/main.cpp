#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int n, m;
    vector<vector<bool>> viz;
    vector<int> di = {-1, 0, 1, 0};
    vector<int> dj = {0, 1, 0, -1};

    bool inMat(int i, int j) { return i >= 0 && i < n && j >= 0 && j < m; }

    void capture(int i, int j, vector<vector<char>>& board) {
        board[i][j] = 'X';
        for (int d = 0; d < 4; d++) {
            int ii = i + di[d];
            int jj = j + dj[d];
            if (inMat(ii, jj) && board[ii][jj] == 'O') 
                capture(ii, jj, board);
        }
    }

    void save(int i, int j, vector<vector<char>>& board) {
        board[i][j] = 'S';
        for (int d = 0; d < 4; d++) {
            int ii = i + di[d];
            int jj = j + dj[d];
            if (inMat(ii, jj) && board[ii][jj] == 'O') 
                save(ii, jj, board);
        }
    }

    void solve(vector<vector<char>>& board) {
        n = board.size();
        m = board[0].size();
        viz = vector<vector<bool>>(n, vector<bool>(m, false));

        if (n < 3 || m < 3) return;


        for (int i = 0; i < n; i++) {
            if (board[i][0] == 'O') save(i, 0, board);
            if (board[i][m-1] == 'O') save(i, m-1, board);
        }

        for (int j = 0; j < m; j++) {
            if (board[0][j] == 'O') save(0, j, board);
            if (board[n-1][j] == 'O') save(n-1, j, board);
        }

        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < m - 1; j++) {
                if (board[i][j] == 'O' && !viz[i][j]) capture(i, j, board);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'S') board[i][j] = 'O';
            }
        }
    }
};


int main() {
    Solution s;
    vector<vector<char>> board = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}
    };
    vector<vector<char>> board2 = {
        {'O', 'O', 'O'},
        {'O', 'O', 'O'},
        {'O', 'O', 'O'}
    };
    s.solve(board2);
    return 0;
}