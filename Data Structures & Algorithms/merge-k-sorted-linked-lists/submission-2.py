# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        
        def merge(arr1, arr2):
            toRet = ListNode(-1)
            pointer = toRet
            left = 0
            right = 0
            iterate = 0

            while arr1 and arr2:
                if arr1.val <= arr2.val:
                    toRet.next = arr1
                    arr1 = arr1.next
                else:
                    toRet.next = arr2
                    arr2 = arr2.next
                toRet = toRet.next
            
            if arr1:
                toRet.next = arr1
            if arr2 :
                toRet.next = arr2
            return pointer.next
        
        currentArr = lists[0]
        for i in range(1, len(lists)):
            currentArr = merge(currentArr, lists[i])
        
        return currentArr