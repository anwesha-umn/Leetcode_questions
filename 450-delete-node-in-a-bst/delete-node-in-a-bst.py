# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

            # Base condition
            if not root:
                return root
            
            if root.val > key: # go to left sub tree
                root.left = self.deleteNode(root.left, key)

            elif root.val < key:
                root.right = self.deleteNode(root.right, key)

            else:
                # if root.val == key

                # cases 1, 2, 3
                if not root.left:
                    return root.right

                elif not root.right:
                    return root.left

                else:
                    # if both left and right sub-trees exist
                    # create a temp sub-tree, go to the left most /right most node to get the replacement value
                    temp = root.left 
                    while temp.right:
                        temp = temp.right

                    # replace current root val
                    root.val = temp.val
                    # delete the duplicate node
                    root.left = self.deleteNode(root.left, temp.val)
            return root
















        # if not root:
        #     return root
        
        # # Using BST property : right child is always > than root
        # if root.val < key:
        #     root.right = self.deleteNode(root.right, key)
        # elif root.val > key:
        #     root.left = self.deleteNode(root.left, key)
        # else:        
        #     # no child case
        #     if not root.left and not root.right:
        #         return None
            
        #     elif root.left and not root.right:
        #         return root.left

        #     elif root.right and not root.left:
        #         return root.right
            
        #     else:
        #         temp = root.left

        #         # find the value that replaces key in temp tree 
        #         while temp.right:
        #             temp = temp.right  # node to replace key value
                
        #         root.val = temp.val   
        #         root.left = self.deleteNode(root.left, temp.val)    # delete the excess temp value from tree
                
        # return root
