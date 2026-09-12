class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        res = []

        first = 0;
        last = len(numbers) - 1

        while first < last:
            if numbers[first] + numbers[last] == target:
                res.append(first + 1)
                res.append(last + 1)
                break
            elif numbers[first] + numbers[last] < target:
                first+=1
            elif numbers[first] + numbers[last] > target:
                last-=1
        
        return res

        