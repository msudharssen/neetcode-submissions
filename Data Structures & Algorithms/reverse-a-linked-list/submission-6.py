# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = head
        prev = None

        while copy:
            nextNode = copy.next
            copy.next = prev
            prev = copy
            copy = nextNode
        return prev
