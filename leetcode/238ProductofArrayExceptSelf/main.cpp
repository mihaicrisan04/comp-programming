#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 0);

        int product = 1;
        for (int i = 0; i < nums.size(); i++) {
            result[i] = product;
            product *= nums[i];
        }

        product = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] *= product;
            product *= nums[i];
        }

        return result;
    }
};


int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4};
    vector<int> nums2 = {-1,1,0,-3,3};
    vector<int> sol = s.productExceptSelf(nums2);
    for (int i: sol) {
        cout << i << ' ';
    }
    return 0;
}