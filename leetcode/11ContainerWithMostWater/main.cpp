#include <bits/stdc++.h>

using namespace std;


class Solution { 
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() -1;
        int Max = -1;
        while (l < r) {
            
            // manual comparisons are a bit faster than std functions
            // if (height[l] <= height[r]) {
            //     if (height[l] * (r - l) > Max) {
            //         Max = height[l] * (r - l);
            //     }
            // }
            // else {
            //     if (height[r] * (r - l) > Max) {
            //         Max = height[r] * (r - l);
            //     }
            // }

            Max = max(Max, min(height[l], height[r]) * (r - l));

            if (height[l] <= height[r]) {
                l++;
            }
            else {
                r--;
            }
        }

        return Max;
    }
};


int main() {
    Solution s;
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    cout << s.maxArea(height);
    return 0;
}