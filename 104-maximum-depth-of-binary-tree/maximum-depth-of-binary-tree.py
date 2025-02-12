# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS - Find left / right node's max depth and add 1 
        # O(n) solution

        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

        # BFS - QUEUE - add root node to queue
        # pop root node from queue - check if root node has a left or right child and append in queue
        from collections import deque

        # Return 0 because an empty subtree has a depth of 0
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1

            for i in range(len(q)):
                node = q.popleft()
                if node.left:     # if left child is present
                    q.append(node.left)
                if node.right:    # if right child is present
                    q.append(node.right)

        return depth

