#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    // linear with l,r vector heights
    // int trap(vector<int>& height) {
    //     vector<int> l(height.size(), 0), r(height.size(), 0);
    //     int ans = 0;

    //     l[0] = height[0];
    //     r[height.size()-1] = height[height.size()-1];

    //     for (int i = 1; i < height.size(); i++) {
    //         l[i] = max(l[i-1], height[i]);
    //     }
    //     for (int i = height.size() - 2; i >= 0; i--) {
    //         r[i] = max(r[i+1], height[i]);
    //     }

    //     for (int i = 1; i < height.size() - 1; i++) {
    //         if (min(l[i-1], r[i+1]) - height[i] > 0) {
    //             ans += min(l[i-1], r[i+1]) - height[i];
    //         }
    //     }

    //     return ans;
    // }

    // two pointer
    int trap(vector<int>& h) {
        int l = 0, r = h.size()-1, lmax = INT_MIN, rmax = INT_MIN, ans = 0;
        while(l < r) {
            lmax = max(lmax, h[l]);
            rmax = max(rmax, h[r]);
            ans += (lmax < rmax) ? lmax - h[l++] : rmax - h[r--];
        }
        return ans;
    }
};  


int main() {
    Solution s;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << s.trap(height);
    return 0;   
}