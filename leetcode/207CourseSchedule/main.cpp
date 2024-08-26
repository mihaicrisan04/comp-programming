#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> visited;
    vector<int> onStack;
    vector<vector<int>> adj;
    bool hasCycle = false;

    void dfs(int v) {
        visited[v] = 1;
        onStack[v] = 1;
        for (int w : adj[v]) {
            if (hasCycle) {
                return;
            }
            if (!visited[w]) {
                dfs(w);
            } else if (onStack[w]) {
                hasCycle = true;
                return;
            }
        }
        onStack[v] = 0;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        visited = vector<int>(numCourses, 0);
        onStack = vector<int>(numCourses, 0);
        adj = vector<vector<int>>(numCourses, vector<int>());
        for (auto p : prerequisites) {
            adj[p[0]].push_back(p[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }
        return !hasCycle;
    }
};

int main() {
    Solution s;
    vector<vector<int>> prerequisites = {{1, 0}, {0, 1}};
    vector<vector<int>> prerequisites2 = {{1, 0}};
    cout << s.canFinish(2, prerequisites) << endl;
    cout << s.canFinish(2, prerequisites2) << endl;
    return 0;
}