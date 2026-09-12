class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        runningTotal = 0
        l = 0

        for r in range(len(arr)):
            runningTotal+=arr[r]
            if r-l+1 > k:
                runningTotal-=arr[l]
                l+=1
            if r-l+1 ==k and runningTotal // k >= threshold:
                    count+=1 
        return count