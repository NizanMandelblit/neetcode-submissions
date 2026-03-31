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
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
        if (!list1 && list2)
            return list2;
        else if (!list2 && list1)
            return list1;

        ListNode *newlist = new ListNode(); // dummy node
        ListNode *newListPtr = newlist;
        ListNode *ptr1 = list1;
        ListNode *ptr2 = list2;
        while (ptr1 && ptr2) {
            if (ptr1->val <= ptr2->val) {
                newListPtr->next = new ListNode(ptr1->val, nullptr);
                ptr1 = ptr1->next;
            }

            else {
                newListPtr->next = new ListNode(ptr2->val, nullptr);
                ptr2 = ptr2->next;
            }
            newListPtr = newListPtr->next;
        }

        if (ptr1)
            newListPtr->next = ptr1;
        else if (ptr2)
            newListPtr->next = ptr2;
        return newlist->next;
    }
};
