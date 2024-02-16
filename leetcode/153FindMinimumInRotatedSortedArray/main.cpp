#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size()-1, Min = INT_MAX;
        while (l < r) {
            int m = (l + r) / 2;
            Min = min(Min, nums[m]);
            if (nums[m] > nums[r]) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }
        return min(Min, nums[l]);
    }
};


int main() {
    Solution s;
    vector<int> nums = {3,4,5,1,2};
    cout << s.findMin(nums) << endl;
    nums = {4,5,6,7,0,1,2};
    cout << s.findMin(nums) << endl;
    nums = {11, 13, 15, 17};
    cout << s.findMin(nums) << endl;
    return 0;
}