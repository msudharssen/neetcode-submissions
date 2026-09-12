class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        info = defaultdict()
        info[0]=1
        

        for num in nums:
            currSum += num
            diff = currSum - k
            if diff in info:
                res += info[diff]
            if currSum not in info:
                info[currSum]=1
            else:
                info[currSum]+=1
            
        return res