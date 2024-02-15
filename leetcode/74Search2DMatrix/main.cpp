#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = -1;
        int l = 0, r = matrix.size() - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (matrix[m][0] <= target && target <= matrix[m][matrix[m].size() - 1]) {
                row = m;
                break;
            }
            if (matrix[m][0] < target) {
                l = m + 1;
                continue;
            }
            if (matrix[m][0] > target) {
                r = m - 1;
                continue;
            }
        }

        if (row == -1) {
            return false;
        }

        l = 0, r = matrix[row].size() - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (matrix[row][m] == target) {
                return true;
            }
            else if (matrix[row][m] < target) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }
        return false;
    }
};


int main() {
    Solution s;
    vector<vector<int>> matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    int target = 3;
    cout << s.searchMatrix(matrix, target) << endl;
    return 0;
}