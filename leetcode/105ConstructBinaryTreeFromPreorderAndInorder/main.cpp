#include<bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    void buildTree(TreeNode*& node, vector<int>& preorder, vector<int>& inorder, int& p, int l, int r) {
        if (l > r) return;

        node = new TreeNode(preorder[p++]);

        int k = 0;
        for (int i = l; i <= r; i++) {
            if (node->val == inorder[i]) {
                k = i;
                break;
            }
        }

        buildTree(node->left, preorder, inorder, p, l, k - 1);
        buildTree(node->right, preorder, inorder, p, k + 1, r);
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        TreeNode* root = nullptr;
        int p = 0;
        buildTree(root, preorder, inorder, p, 0, inorder.size() - 1);
        return root;
    }
};


void printTree(TreeNode* root) {
    if (root == nullptr) return;
    printTree(root->left);
    cout << root->val << " ";
    printTree(root->right);
}

int main() {
    Solution s;
    vector<int> preorder = {3,9,20,15,7};
    vector<int> inorder = {9,3,15,20,7};
    TreeNode* root = s.buildTree(preorder, inorder);
    printTree(root);
    return 0;
}