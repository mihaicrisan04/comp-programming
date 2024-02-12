#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == nums[i-1] && i > 0) {
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                if (nums[l] == nums[l-1] && l > i + 1) {
                    l++;
                    continue;
                }
                if (nums[r] == nums[r+1] && r < nums.size() - 1) {
                    r--;
                    continue;
                }

                if (nums[l] + nums[r] == -nums[i]) {
                    result.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                }
                else if (nums[l] + nums[r] < -nums[i]) {
                    l++;
                }
                else {
                    r--;
                }
            }
        }
        return result;
    }
};


int main() {
    Solution s;
    vector<int> nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> ans = s.threeSum(nums);
    // print the answer
    for (const auto& triplet : ans) {
        for (const auto& num : triplet) {
            cout << num << " ";
        }
        cout << endl;
    }
    
    return 0;
}