#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int goodNodes(TreeNode* root, int maxValue = -1e9) {
        if (root) return (root->val >= maxValue) + goodNodes(root->left, max(maxValue, root->val)) + goodNodes(root->right, max(maxValue, root->val));
        return 0;
    } 
};


int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->left->left = new TreeNode(3);
    root->right->left = new TreeNode(1);
    root->right->right = new TreeNode(5);
    Solution s;
    std::cout << s.goodNodes(root) << std::endl;
    return 0;
}