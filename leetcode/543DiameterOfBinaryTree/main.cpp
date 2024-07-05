#include<bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxi = 0;
    int dfs(TreeNode* root) {
        if (!root) return 0;
        int dl = dfs(root->left);
        int dr= dfs(root->right);
        maxi = max(maxi, dl + dr);
        return max(dl, dr) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return maxi;
    }
};


int main() {
    Solution s;
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    cout << s.diameterOfBinaryTree(root) << endl;
    return 0;
}