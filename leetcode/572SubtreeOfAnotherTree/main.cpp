#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public: 
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        bool res = isSubtreeHelper(root, subRoot);
        if (res) return true;
        if (!root) return false;
        else return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

    bool isSubtreeHelper(TreeNode* a, TreeNode* b) {
        if (a && b) {
            if (a->val == b->val) return true && isSubtreeHelper(a->left, b->left) && isSubtreeHelper(a->right, b->right);
            else return false;
        }
        else if (!a && !b) return true;
        else return false;
    }
};


int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(4);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(2);
    root->left->right->left = new TreeNode(0);
    Solution sol;
    cout << sol.isSubtree(root, root->left) << endl;
    return 0;
}