#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    void dfs(vector<string>& ans, string s, int left, int right, int n) {
        if (left == n && right == n) {
            ans.push_back(s);
            return;
        }
        if (left < n) {
            dfs(ans, s + '(', left + 1, right, n);
        }
        if (right < left) {
            dfs(ans, s + ')', left, right + 1, n);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string s = "";
        dfs(ans, s, 0, 0, n);
        return ans;
    }
};


int main() {
    Solution s;
    vector<string> ans = s.generateParenthesis(3);
    for (string i : ans) {
        cout << i << ' ';
    }
    return 0;
}