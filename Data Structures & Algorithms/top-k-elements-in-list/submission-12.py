class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iterate = [[] for i in range(len(nums)+1)]
        freq = Counter(nums)

        for key, val in freq.items():
            iterate[val].append(key)
        
        output = []
        for i in range(len(iterate)-1,0,-1):
            for num in iterate[i]:
                output.append(num)
                if len(output)==k:
                    return output
        return output

        
