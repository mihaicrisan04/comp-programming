#include<bits/stdc++.h>

using namespace std;

/// work in progress

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> q;
    int k;

    KthLargest(int k, vector<int>& nums) : k(k) {

    }

    int add(int val) {
        q.push(val);
        if (q.size() > k) {
            q.pop();
        }
        return q.top();
    }
    
};


int main() {
    vector<int> nums = {4, 5, 8, 2};
    KthLargest kthLargest(3, nums);
    cout << kthLargest.add(3) << endl;
    cout << kthLargest.add(5) << endl;
    cout << kthLargest.add(10) << endl;
    cout << kthLargest.add(9) << endl;
    cout << kthLargest.add(4) << endl;
    return 0;
}