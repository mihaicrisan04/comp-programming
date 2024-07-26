#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        while (head) {    
            ListNode* next = head->next;
            ListNode* prev = head; 
            while (next) {
                prev = next;
                next = next->next;
            }
            prev->next = nullptr;           
            ListNode* aux = head->next;
            head->next = next;
            next->next = aux;
            head = aux->next;
        }
    } 
};


int main() {
    Solution s;
    ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
    s.reorderList(head);
    while (head) {
        cout << head->val << " ";
        head = head->next;
    }
    return 0;
}