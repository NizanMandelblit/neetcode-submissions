# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # it's given that root !=null
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr=curr.right
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:  # eiter a split happens, or we reached the p or q itself
                return curr

        