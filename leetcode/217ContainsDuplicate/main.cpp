#include <iostream>
#include <vector>   
#include <algorithm>


class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
};


int main() {
    Solution solution;
    std::vector<int> nums = {1, 2, 3, 1};
    std::cout << solution.containsDuplicate(nums) << std::endl;
    return 0;
}