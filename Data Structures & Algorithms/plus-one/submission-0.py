class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for r in range(len(digits)-1,-1,-1):
            if digits[r]==9:
                digits[r]=0
            else:
                digits[r]=digits[r]+1
                return digits
        res = [0]*(len(digits)+1)
        res[0]=1
        return res



