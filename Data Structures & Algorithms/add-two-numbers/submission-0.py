# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        iterate = ListNode(-1)
        third = iterate
        carry = 0

        while first or second or carry:
            val1 = first.val if first else 0
            val2 = second.val if second else 0
            total = val1 + val2 + carry
            carry = total//10
            digitToAdd = total % 10
            iterate.next = ListNode(digitToAdd)
            iterate = iterate.next
            first = first.next if first else None
            second = second.next if second else None
        return third.next
            
            