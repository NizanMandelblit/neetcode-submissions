# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Preorder (Root-Left-Right), Inorder (Left-Root-Right), and Postorder (Left-Right-Root)
        # The first element of the preorder array is always the root.
        #  We can find this root's position in the inorder array, which divides inorder into left and right subtrees.
        #  Elements before the root in inorder belong to the left subtree, and elements after belong to the right subtree.
        # The same split applies to preorder.
        #  We recursively build left and right subtrees using the corresponding portions of both arrays.
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
