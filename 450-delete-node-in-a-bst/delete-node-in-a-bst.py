# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        
        # Using BST property : right child is always > than root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:        
            # no child case
            if not root.left and not root.right:
                return None
            
            elif root.left and not root.right:
                return root.left

            elif root.right and not root.left:
                return root.right
            
            else:
                temp = root.left

                # find the value that replaces key in temp tree 
                while temp.right:
                    temp = temp.right  # node to replace key value
                
                root.val = temp.val   
                root.left = self.deleteNode(root.left, temp.val)    # delete the excess temp value from tree
                
        return root
