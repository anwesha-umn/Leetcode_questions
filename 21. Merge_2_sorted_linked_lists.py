# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        merged = ListNode(0) #head node with val=0
        # copy merged Linkedlist into another linked list  (we want to return head of merged list)
        copy_merged = merged

        head1 = list1
        head2 = list2

        #loop if any of them is not empty
        while head1 or head2:
            if head1 and head2:                     # if both are not empty
                if head1.val < head2.val:           # check which head has lower value and add to merged.next 
                    merged.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    merged.next = ListNode(head2.val)        
                    head2 = head2.next

            elif head1:                             # if head1 is not empty/ head2 is empty
                merged.next = ListNode(head1.val)
                head1 = head1.next
            elif head2:
                merged.next = ListNode(head2.val)   # if head2 is not empty/ head1 is empty
                head2 = head2.next

            merged = merged.next
        return copy_merged.next                    # return head of copy_merged
