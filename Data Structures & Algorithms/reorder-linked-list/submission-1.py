# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second = slow.next
        slow.next=None

        # reverse second half
        prev= None
        while second:
            tmp = second.next
            second.next=prev
            prev=second
            second = tmp

        # merge
        first = head
        second=prev # prev is the head of the revesed second half list
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next=second
            second.next=tmp1
            second = tmp2
            first=tmp1


