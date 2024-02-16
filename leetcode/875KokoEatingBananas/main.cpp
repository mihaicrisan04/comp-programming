#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long l = 1, r = 0;
        for (long unsigned int i = 0; i < piles.size(); i++) {
            r = max((int)r, piles[i]);
        }

        while (l <= r) {
            long long m = (l + r) / 2;
            
            long long k = 0;
            for (int i = 0; i < piles.size(); i++) {
                k += (piles[i] % m == 0) ? piles[i] / m : piles[i] / m + 1;
            }

            if (k <= h) {
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        return (int)l;
    }
};


int main() {
    Solution s;
    vector<int> piles = {3, 6, 7, 11};
    int h = 8;
    cout << s.minEatingSpeed(piles, h) << endl;
    piles = {30, 11, 23, 4, 20};
    h = 6;
    cout << s.minEatingSpeed(piles, h) << endl;
    return 0;
}