"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew= {}
        def dfs(currNode):
            if currNode in oldToNew:
                return oldToNew[currNode]
            
            copy = Node(currNode.val)
            oldToNew[currNode] = copy
            for neighbor in currNode.neighbors:
                copyNodeNeighbor = dfs(neighbor)
                copy.neighbors.append(copyNodeNeighbor)
            return copy

        return dfs(node)

        