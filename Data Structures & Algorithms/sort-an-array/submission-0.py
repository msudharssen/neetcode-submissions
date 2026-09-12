class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                # arr[j] and arr[j + 1] are out of order so swap them 
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                j -= 1
        return arr