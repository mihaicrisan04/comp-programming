#include<bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && q || !q && p) return false;
        else if (p && q) return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        else return true;
    }
};


int main() {
    Solution s;
    TreeNode *p = new TreeNode(1);
    p->left = new TreeNode(2);
    p->right = new TreeNode(3);
    TreeNode *q = new TreeNode(1);
    q->left = new TreeNode(2);
    q->right = new TreeNode(3);
    cout << s.isSameTree(p, q) << endl;
    return 0;
}