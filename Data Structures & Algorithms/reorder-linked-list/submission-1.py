# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        hold = []
        temp = head
        while temp:
            hold.append(temp)
            temp = temp.next 
        l = 0
        r = len(hold)-1
        
        while l < r:
            hold[l].next = hold[r]
            l+=1
            if l>=r:
                break
            hold[r].next = hold[l]
            r-=1
        
        hold[l].next = None
        