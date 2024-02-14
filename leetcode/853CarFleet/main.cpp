#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<float> st;
        vector<pair<int, int>> cars;

        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }

        sort(cars.begin(), cars.end(), [](pair<int, int> a, pair<int, int> b) {
            return a.first < b.first;
        });

        for (int i = cars.size() - 1; i >= 0; i--) {
            st.push_back((float)(target - cars[i].first) / cars[i].second);
            if (st.size() > 1 && st[st.size() - 1] <= st[st.size() - 2]) {
                st.pop_back();
            }
        }
        return st.size();
    }
};


int main() {
    Solution s;
    vector<int> position = {10, 8, 0, 5, 3};
    vector<int> speed = {2, 4, 1, 1, 3};
    cout << s.carFleet(12, position, speed) << endl;
    return 0;
}