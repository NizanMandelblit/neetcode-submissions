# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # the max diameter
        
        # returns height of tree
        def dfs(curr):
            if not curr:
                return 0
            
            leftHeigt= dfs(curr.left)
            rightHeight= dfs(curr.right)
            self.res = max(self.res, leftHeigt + rightHeight) # save the longest path so far

            return 1 + max(leftHeigt,rightHeight)

    
        dfs(root)
        return self.res

