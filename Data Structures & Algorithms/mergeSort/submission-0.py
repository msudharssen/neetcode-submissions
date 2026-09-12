# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs)<=1:
            return pairs
        
        mid = len(pairs)//2
        firstArray = self.mergeSort(pairs[:mid])
        secondArray = self.mergeSort(pairs[mid:])
        return  self.merge(firstArray, secondArray)
    
    def merge(self, firstA, secondA):
        leftPointer = 0
        rightPointer = 0
        output = []

        while leftPointer < len(firstA) and rightPointer < len(secondA):
            if firstA[leftPointer].key <= secondA[rightPointer].key:
                output.append(firstA[leftPointer])
                leftPointer+=1
            else:
                output.append(secondA[rightPointer])
                rightPointer+=1
        
        while leftPointer < len(firstA):
            output.append(firstA[leftPointer])
            leftPointer+=1
        while rightPointer < len(secondA):
            output.append(secondA[rightPointer])
            rightPointer+=1
        
        return output




