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
        ListNode* s = head;
        ListNode* f = head->next;
        while (f && f->next) {
            s = s->next;
            f = f->next->next;
        }
        ListNode* sec = s->next;
        s->next = NULL;
        ListNode* prev = NULL;
        while (sec) {
            ListNode* temp = sec->next;
            sec->next = prev;
            prev = sec;
            sec = temp;
        }
        ListNode* second = prev;
        ListNode* first;
        while (second) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
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