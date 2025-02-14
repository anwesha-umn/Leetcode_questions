# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        dummy = head

        twin_list = []
        while head:
            twin_list.append(head.val)
            head = head.next

        max_sum = 0
        n= len(twin_list)
        for i in range(len(twin_list)):
            max_sum = max(max_sum, twin_list[i]+twin_list[n-1-i])

        return max_sum
