/*
 * @lc app=leetcode id=23 lang=cpp
 *
 * [23] Merge k Sorted Lists
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
// using namespace std;
// #include <vector>
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode(): val(0), next(nullptr) {}
//     ListNode(int x): val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next): val(x), next(next) {}
// };
class Solution {
  public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.empty())
            return nullptr;
        while (lists.size() > 1) {
            vector<ListNode *> mergedLists;
            for (size_t i = 0; i < lists.size(); i += 2) {
                ListNode *l1 = lists[i];
                ListNode *l2 = (i + 1 < lists.size()) ? lists[i + 1] : nullptr;
                mergedLists.push_back(mergeTwoLists(l1, l2));
            }
            lists = mergedLists;
        }

        return lists[0];
    }

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
// @lc code=end
