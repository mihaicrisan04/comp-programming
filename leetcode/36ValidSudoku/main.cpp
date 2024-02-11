#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    /**
     * Checks if a given Sudoku board is valid.
     *
     * @param board The Sudoku board represented as a 2D vector of characters.
     * @return True if the Sudoku board is valid, false otherwise.
     */
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> row(9), col(9), box(9);  // 9 rows, 9 columns, 9 boxes
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                char c = board[i][j];
                if(c == '.') continue;
                if(row[i].count(c) || col[j].count(c) || box[i/3*3+j/3].count(c)) return false;
                row[i].insert(c);
                col[j].insert(c);
                box[i/3*3+j/3].insert(c);
            }
        }
        return true;
    }
};


int main() {
    Solution s;
    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };
    cout << s.isValidSudoku(board) << endl;
    return 0;
}