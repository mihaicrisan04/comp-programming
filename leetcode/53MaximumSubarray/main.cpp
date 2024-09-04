#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = -1e9;
        int sum = 0;

        for (int num: nums) {
            sum += num;
            maxSum = max(sum, maxSum);
            if (sum < 0) sum = 0;
        }

        return maxSum;
    }
};


int main() {
    Solution s;
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    cout << s.maxSubArray(nums) << endl;
    vector<int> nums2 = {1};
    cout << s.maxSubArray(nums2) << endl;
    vector<int> nums3 = {5,4,-1,7,8};
    cout << s.maxSubArray(nums3) << endl;
    return 0;
}