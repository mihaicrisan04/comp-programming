#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        int longest_consec = 0;

        for (int num : s) {
            if (!s.count(num - 1)) {  // if the number is the start of a sequence
                int current_num = num;
                int current_consec = 1;

                while (s.count(current_num + 1)) {
                    current_num++;
                    current_consec++;
                }

                longest_consec = max(longest_consec, current_consec);
            }
        }

        return longest_consec;
    }
};


int main() {
    Solution s;

    vector<int> nums = {0,3,7,2,5,8,4,6,0,1};
    cout << s.longestConsecutive(nums);

    return 0;
}