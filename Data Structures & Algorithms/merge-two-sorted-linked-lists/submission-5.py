# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start1 = list1
        start2 = list2

        result = ListNode()
        result2 = result

        while start1 and start2:
            if start1.val <= start2.val:
                result.next = start1
                start1 = start1.next
            else:
                result.next = start2
                start2 = start2.next
            result = result.next
        
        if start1:
            result.next = start1
        elif start2:
            result.next = start2
        
        return result2.next