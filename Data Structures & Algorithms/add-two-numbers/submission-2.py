# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, None)
        carry = 0
        curr = dummy

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curr.next = ListNode((val1 + val2 + carry) % 10) # Get the digits place
            carry = (val1 + val2 + carry ) // 10 # Get the carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next


        if carry:
            curr.next = ListNode(1)


        return dummy.next