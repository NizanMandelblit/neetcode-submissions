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

class Solution {
public:
    void reorderList(ListNode *head) {
        if (!head || !head->next || !head->next->next)
            return; // Return early if the list has fewer than 3 nodes

        // split into halves
        ListNode *slowPtr = head;
        ListNode *fastPtr = head;
        while (fastPtr && fastPtr->next) {
            slowPtr = slowPtr->next;
            fastPtr = fastPtr->next->next;
        }

        // reverse second half
        ListNode *secondHalfPtrHead = slowPtr->next;
        slowPtr->next = nullptr; // Split the list into two parts
        ListNode *firstHalfPtrHead = head;

        ListNode *curr = secondHalfPtrHead;
        ListNode *tmp;
        ListNode *prev = nullptr;

        while (curr) {
            tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        secondHalfPtrHead = prev;

        // merge
        ListNode *firstHalfPtr = firstHalfPtrHead;
        ListNode *secondHalfPtr = secondHalfPtrHead;
        ListNode *tmp1;
        ListNode *tmp2;
        while (secondHalfPtr) {
            tmp1 = firstHalfPtr->next;
            firstHalfPtr->next = secondHalfPtr;
            tmp2 = secondHalfPtr->next;
            secondHalfPtr->next = tmp1;

            firstHalfPtr = tmp1;
            secondHalfPtr = tmp2;
        }
    }
};
