# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = {} # node:visited

        curr = head
        while curr:
            if hashSet.get(curr,0) == 1:
                return True
            hashSet[curr] = 1
            curr = curr.next

        return False






        # slow, fast = head, head

        # while fast and fast.next:
        #     fast=fast.next.next
        #     slow=slow.next
        #     if fast==slow:
        #         return True
        
        # return False