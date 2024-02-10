#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for (string s : strs) {
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            anagrams[sorted].push_back(s);
        }
        vector<vector<string>> result;
        for (auto it = anagrams.begin(); it != anagrams.end(); it++) {
            result.push_back(it->second);
        }
        return result;
    }
};


int main() {
    Solution sol;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = sol.groupAnagrams(strs);
    for (vector<string> group : result) {
        for (string s : group) {
            cout << s << " ";
        }
        cout << endl;
    }
    return 0;
}