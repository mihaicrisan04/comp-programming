#include<bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<pair<int, TreeNode*>> q;
        q.push({0, root});

        while (!q.empty()) {
            int level = q.front().first;
            TreeNode* node = q.front().second;
            q.pop();

            if (!node) continue;

            if (res.size() == level) {
                res.push_back({});
            }
            res[level].push_back(node->val);

            q.push({level + 1, node->left});
            q.push({level + 1, node->right});
        }

        return res;
    }
};


int main() {
    Solution s;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    vector<vector<int>> res = s.levelOrder(root);
    for (auto v : res) {
        for (int i : v) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}