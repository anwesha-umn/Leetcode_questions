# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # using slow and fast pointers
        slow = head
        fast = head.next
        
        if head.next==None:
            return None

        while fast.next!=None and fast.next.next!=None:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        return head