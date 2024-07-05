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
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        int hl = h(root->left);
        int hr = h(root->right);
        return abs(hl - hr) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    }

    int h(TreeNode *root) {
        if (!root) return 0;
        int hr = h(root->right);
        int hl = h(root->left);
        return max(hr, hl) + 1;
    }
};


int main() {
    Solution s;
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    cout << s.isBalanced(root) << endl;

    return 0;
}