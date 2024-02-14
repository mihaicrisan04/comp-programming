#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> output(temperatures.size(), 0);
        stack<pair<int,int>> st;

        for (int i = 0; i < temperatures.size(); i++) {
            while (!st.empty() && st.top().first < temperatures[i]) {
                output[st.top().second] = i - st.top().second;
                st.pop(); 
            }
            st.push({temperatures[i], i});
        }
        
        return output;
    }
};


int main() {
    Solution s;
    vector<int> temperatures = {73,74,75,71,69,72,76,73};
    vector<int> output = s.dailyTemperatures(temperatures);
    for (int i : output) {
        cout << i << ' ';
    }
    return 0;
}