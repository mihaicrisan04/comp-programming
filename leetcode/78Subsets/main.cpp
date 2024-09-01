#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> sol;
    vector<int> curr;

    void back(int k, vector<int>& nums) {
        sol.push_back(curr);
        for (int i = k; i < nums.size(); i++) {
            curr.push_back(nums[i]);
            back(i + 1, nums);
            curr.pop_back();
        } 
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        back(0, nums);
        return sol;
    }
};


int main() {
    Solution s;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> sol = s.subsets(nums);
    for (auto set: sol) {
        for (auto i: set)
            cout << i << ' ';
        cout << endl;
    }
    return 0;
}