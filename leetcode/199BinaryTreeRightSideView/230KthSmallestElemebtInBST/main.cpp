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
    priority_queue<int, vector<int>, greater<int>> q;

    int kthSmallest(TreeNode* root, int k) {
        dfs(root);
        while (--k && !q.empty()) q.pop();
        return q.top();
    }

    void dfs(TreeNode* node) {
        if (node) {
            q.push(node->val);
            dfs(node->left);
            dfs(node->right);
        }
    }
};


int main() {
    Solution s;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->left->right = new TreeNode(2);
    cout << s.kthSmallest(root, 1) << endl;
    return 0;
}