#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0;
        int curr = 0;
        int next = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            next = max(prev + nums[i], curr);
            prev = curr;
            curr = next;
        }
        
        return curr;
    } 
};


int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 1};
    cout << s.rob(nums) << endl;
    vector<int> nums2 = {2, 7, 9, 3, 1};    
    cout << s.rob(nums2) << endl;
    vector<int> nums3 = {2, 1, 1, 2};
    cout << s.rob(nums3) << endl;
    return 0;
}