# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

       # need to create a function that appends values of leaf nodes to list recursively
        def leafnode(root, leaf_vals):
            if not root:                   # if root is None
                return root
            if not root.left and not root.right:          # check if there are no child nodes
                leaf_vals.append(root.val)
                
            leafnode(root.left, leaf_vals)
            leafnode(root.right, leaf_vals)

        root1_leaf = []
        root2_leaf = []

        leafnode(root1, root1_leaf)
        leafnode(root2, root2_leaf)

        return root1_leaf == root2_leaf