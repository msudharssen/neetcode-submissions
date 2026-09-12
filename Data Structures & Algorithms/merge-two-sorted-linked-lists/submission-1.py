# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = list1
        temp2 = list2
        start = ListNode(-1)
        begin = start

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                start.next = temp1
                temp1 = temp1.next
            else:
                start.next = temp2
                temp2 = temp2.next
            start = start.next
        
        while temp1:
            start.next = temp1
            start = start.next
            temp1 = temp1.next
        while temp2:
            start.next = temp2
            start = start.next
            temp2 = temp2.next
        return begin.next
