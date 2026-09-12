class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        currSum = 0
        l = 0

        for r in range(len(arr)):
            currSum+=arr[r]
            if r-l+1 > k:
                currSum -= arr[l]
                l+=1
            if r-l+1 == k and currSum/k >= threshold:
                res+=1
        return res