# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True

            # The current node's value must be strictly within the range
            if not (low < node.val < high):
                return False

            # Left child must be < node.val
            # Right child must be > node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Start with negative and positive infinity as boundaries
        return validate(root, float("-inf"), float("inf"))
