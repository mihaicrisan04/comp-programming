#include<bits/stdc++.h>


using namespace std;


class TimeMap {
public:
    unordered_map<string, vector<pair<int,string>>> m;

    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        m[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        auto it = upper_bound(m[key].begin(), m[key].end(), timestamp, [](int t, pair<int,string> p) { return t < p.first; });
        return it == m[key].begin() ? "" : prev(it)->second;
    }
};


int main() {


    return 0;
}