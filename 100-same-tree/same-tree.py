# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       
        # DFS - RECURSION - O(N)
        if not p and not q:   # if both nodes are null - return True
            return True

        if p and q and p.val == q.val:   # if root values are same go to child nodes
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # if above 2 conditions are not True
        return False

