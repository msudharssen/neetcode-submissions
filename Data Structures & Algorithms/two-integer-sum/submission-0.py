class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}
        res = []

        for i, item in enumerate(nums):
            balance = target - item
            if balance in store:
                res.append(store[balance])
                res.append(i)
                break
            else:
                store[item] = i
        
        return res

        