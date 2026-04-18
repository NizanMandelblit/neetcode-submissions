# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recurisve On time and space
        if not head:
            return None
        # ->1->2
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next=None
        return newHead


        # iteartive O n time O1 space
        # prev, curr = None, head

        # while curr:
        #     tmp = curr.next
        #     curr.next = prev
        #     prev =curr
        #     curr = tmp
        # return prev