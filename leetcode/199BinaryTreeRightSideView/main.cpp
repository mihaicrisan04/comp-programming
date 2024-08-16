#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        bitset<105> depthSet;
        vector<int> ans;
        dfs(root, 0, ans, depthSet);
        return ans;
    }

    void dfs(TreeNode* node, int depth, vector<int>& ans, bitset<105>& depthSet) {  
        if (node) {
            if (!depthSet[depth])  {
                ans.push_back(node->val);
                depthSet[depth] = 1;
            }
            dfs(node->right, depth + 1, ans, depthSet);
            dfs(node->left, depth + 1, ans, depthSet);
        }
    }
};


int main() {
    Solution s;
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->right = new TreeNode(5);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(4);
    vector<int> ans = s.rightSideView(root);
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    return 0;
}