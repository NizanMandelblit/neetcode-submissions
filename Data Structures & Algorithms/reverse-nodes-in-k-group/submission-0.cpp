/*
 * @lc app=leetcode id=25 lang=cpp
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode(): val(0), next(nullptr) {}
//     ListNode(int x): val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next): val(x), next(next) {}
// };
class Solution {
  public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        ListNode *dummy = new ListNode(0, head);
        ListNode *groupPrev = dummy;

        while (true) {
            ListNode *kth = getKth(groupPrev, k);
            if (!kth)
                break;
            ListNode *groupNext = kth->next;

            ListNode *curr = groupPrev->next;
            ListNode *prev = kth->next; // usually this would be nullptr
            while (curr != groupNext) {
                ListNode *tmp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = tmp;
            }

            ListNode *tmp =
                groupPrev->next; // in the k-th group used to be our first, now it's last
            groupPrev->next = kth;
            groupPrev = tmp;
        }

        return dummy->next;
    }

    ListNode *getKth(ListNode *head, int k) {
        ListNode *ptr = head;
        while (ptr && k > 0) {
            ptr = ptr->next;
            k--;
        }

        return ptr;
    }
};
// @lc code=end
