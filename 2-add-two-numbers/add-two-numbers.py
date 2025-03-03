# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = dummy  = ListNode(0)
        s = 0
        carry = 0
        
        # check if numbers are left in l1 and l2 or any carryover is left
        while l1 or l2 or carry:

            s = carry   # start summing with carry over digit
            if l1:
                s += l1.val
                l1 = l1.next
            if l2: 
                s += l2.val
                l2 = l2.next

            rem = s % 10
            carry = s//10

            new.next = ListNode(rem)
            new = new.next            

        return dummy.next

        