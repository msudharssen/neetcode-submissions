class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n==1:
                return True
        return False
    
    def sumOfSquares(self, number):

        ans = 0
        temp = number

        while temp:
            lastDigit = temp % 10
            ans = ans + (lastDigit * lastDigit)
            temp = temp // 10
        
        return ans
