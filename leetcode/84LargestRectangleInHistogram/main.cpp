#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max_area = 0;
        stack<pair<int,int>> st;

        for (int i = 0; i < heights.size(); i++) {
            int start = i;
            while (!st.empty() && st.top().second > heights[i]) {
                max_area = max(max_area, (i - st.top().first) * st.top().second);
                start = st.top().first;
                st.pop();
            }
            st.push({start, heights[i]});
        }

        while (!st.empty()) {
            max_area = max(max_area, (int)((heights.size() - st.top().first) * st.top().second));
            st.pop();
        }

        return max_area;
    }
};


int main() {
    Solution s;
    vector<int> heights = {2,1,5,6,2,3};
    cout << s.largestRectangleArea(heights) << endl;
    return 0;
}