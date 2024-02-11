#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        while (l != r) {
            if (numbers[l] + numbers[r] == target) {
                return {l + 1, r + 1};
            }
            else if (numbers[l] + numbers[r] < target) {
                l++;
            }
            else {
                r--;
            }
        }
        return {-1, -1};
    }
};


int main() {
    Solution s;
    vector<int> numbers = {2, 7, 11, 15};
    vector<int> numbers2 = {2, 3, 4};
    vector<int> numbers3 = {-1, 0};

    vector<int> ans = s.twoSum(numbers, 9);
    vector<int> ans2 = s.twoSum(numbers2, 6);
    vector<int> ans3 = s.twoSum(numbers3, -1);
    for (long unsigned int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
    for (long unsigned int i = 0; i < ans2.size(); i++) {
        cout << ans2[i] << " ";
    }
    cout << endl;
    for (long unsigned int i = 0; i < ans3.size(); i++) {
        cout << ans3[i] << " ";
    }

    return 0;
}