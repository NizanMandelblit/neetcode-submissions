/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node *copyRandomList(Node *head) {
        if (!head)
            return nullptr;

        unordered_map<Node *, Node *> hashMap; // links original node to copied.
        Node *cloned_head = new Node(head->val);
        hashMap[head] = cloned_head;

        // build copied list `next` field
        Node *ptr_copy = cloned_head;
        Node *ptr_original = head->next;
        while (ptr_original) {
            ptr_copy->next = new Node(ptr_original->val);
            hashMap[ptr_original] = ptr_copy->next;
            ptr_original = ptr_original->next;
            ptr_copy = ptr_copy->next;
        }

        // fill up random ptrs using the hashMap
        ptr_original = head;
        ptr_copy = cloned_head;
        while (ptr_original) {
            ptr_copy->random = hashMap[ptr_original->random];
            ptr_original = ptr_original->next;
            ptr_copy = ptr_copy->next;
        }

        return cloned_head;
    }
};
