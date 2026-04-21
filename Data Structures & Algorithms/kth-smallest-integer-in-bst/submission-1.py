# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # brute force - collect all values, sort, return arr[k-1]
        # # O n*logn
        # self.arr = []

        # def dfs(root):
        #     if not root:
        #         return
        #     self.arr.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        # self.arr.sort()
        # return self.arr[k-1]

        # in order traversel O n
        arr = []

        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            arr.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return arr[k-1]