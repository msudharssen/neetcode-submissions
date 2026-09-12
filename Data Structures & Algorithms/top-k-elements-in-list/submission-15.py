class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = Counter(nums)

        allFreq = [[] for i in range(len(nums)+1)]

        for numb, freq in frequencies.items():
            allFreq[freq].append(numb)
        

        res = []

        for i in range(len(allFreq)-1,-1,-1):
            for num in allFreq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return res
            