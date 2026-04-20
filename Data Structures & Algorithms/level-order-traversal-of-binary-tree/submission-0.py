# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # list of lists, example [[1],[2,3],[4,5,6,7]]
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            curr_level_vales = []
            for i in range(level_size):
                curr = queue.popleft()
                curr_level_vales.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr_level_vales)
            
        return res


