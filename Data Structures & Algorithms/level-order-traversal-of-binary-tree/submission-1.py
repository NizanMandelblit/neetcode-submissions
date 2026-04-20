# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        # Initialize queue with the root
        queue = deque([root])

        while queue:
            level_size = len(queue)
            curr_level_values = []  

            for i in range(level_size):
                curr = queue.popleft()
                curr_level_values.append(curr.val)

                # Add children to queue for the next iteration of the while loop
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # Append the full level to our result list
            res.append(curr_level_values)

        return res
