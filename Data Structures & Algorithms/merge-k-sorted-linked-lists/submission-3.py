# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(array, index):
            copy = array
            iterate = copy
            temp = ListNode(-1)
            second = temp
            copySecond = lists[index]
            iterate2 = copySecond
            while copy and copySecond:
                if copy.val <= copySecond.val:
                    second.next = copy
                    copy = copy.next
                else:
                    second.next = copySecond
                    copySecond = copySecond.next
                second = second.next
            if copy:
                second.next = copy
            if copySecond:
                second.next = copySecond
            return temp.next
        
        mergedArray = lists[0]
        ind = 1
        while ind < len(lists):
            currArray = merge(mergedArray, ind)
            mergedArray = currArray
            ind+=1
        return mergedArray