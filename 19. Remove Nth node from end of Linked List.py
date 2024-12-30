# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first method
        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next

        # node = len(l) - n

        # new = dummy = ListNode(0)

        # for i in range(len(l)):
        #     if i!=node:
        #         new.next = ListNode(l[i])
        #         new = new.next
        # return dummy.next


        # second method: skipping nth node using 2 ListNodes
        first = second = dummy = ListNode(0)
        first.next = head

        for i in range(n+1):
            first = first.next    #brings first pointer to nth node to be removed

        while first:             # this creates gap between first and second pointers of n digits
            first = first.next
            second = second.next  

        # now when first node reaches end of list
        second.next = second.next.next

        return dummy.next


        
