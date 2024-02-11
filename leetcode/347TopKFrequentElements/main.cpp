#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> f;
        vector<int> v;

        for (int i: nums) {
            f[i]++;
        }

        vector<pair<int, int>> p(f.begin(), f.end());
        sort(p.begin(), p.end(), [this](pair<int,int>& a, pair<int,int>& b) {
            return a.second > b.second;
        });

        for (int i = 0; i < k; i++) {
            v.push_back(p[i].first);
        }

        return v;
    }
};


int main() {
    Solution solution;
    vector<int> v = {1, 1, 1, 2, 2, 3};
    int k = 2;

    vector<int> sol = solution.topKFrequent(v, k);

    for (int i: sol) {
        cout << i << ' ';
    }
    return 0;
}