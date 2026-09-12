class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        ans = []
        info = Counter(nums)

        for key, val in info.items():
            if val > len(nums)//3:
                ans.append(key)
        return ans