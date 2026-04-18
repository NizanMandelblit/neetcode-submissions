# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseRecursive(self, prev, curr):
        if not curr:
            return prev

        tmp = curr.next

        curr.next=prev
        prev=curr

        return self.reverseRecursive(prev,tmp)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseRecursive(None, head)
