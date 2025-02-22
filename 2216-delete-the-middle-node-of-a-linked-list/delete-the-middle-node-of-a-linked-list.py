# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # take slow and fast pointers
        slow = head
        fast = head.next

        if head.next is None:
            return None

        while fast.next!= None and fast.next.next!=None:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        return head