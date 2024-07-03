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
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return root;
        TreeNode* aux = root->left; 
        root->left = root->right;
        root->right = aux;
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        return root;
    }
};


int main() {
    Solution s;

    return 0;
}