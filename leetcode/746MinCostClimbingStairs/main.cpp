#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size(), 1e9);
        dp[0] = cost[0];
        dp[1] = cost[1];

        for (int  i = 2; i < cost.size(); i++) {
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i];
        }

        return min(dp[cost.size() - 2], dp[cost.size() - 1]);
    }
};


int main() {
    Solution s;
    vector<int> cost = {10, 15, 20};    
    cout << s.minCostClimbingStairs(cost) << endl;
    vector<int> cost2 = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
    cout << s.minCostClimbingStairs(cost2) << endl;

    return 0;
}