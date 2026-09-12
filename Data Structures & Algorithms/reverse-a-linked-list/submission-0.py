# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        first = None

        while temp:
            curr = temp.next
            temp.next = first
            first = temp
            temp = curr
        
        return first