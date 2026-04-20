# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion, using stack...
        # O logn for balanced tree, O N for degenerate tree)
        if not root:
            return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # stack without recursion
        stack = [] # paris of (node, depth of that node)
        stack.append((root,1))
        res = 0
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1)) 

        return res

