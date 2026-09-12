class Solution:
    def reverse(self, x: int) -> int:
        def computeReverse(x):
            val = 0
            while x:
                lastDigit = x % 10
                x = x // 10
                if val > (2**31 -1 - lastDigit) // 10:
                    return 0
                val = val * 10 + lastDigit
            return val
        
        if x < int(math.pow(-2, 31)) or x>int(math.pow(2,31))-1:
            return 0
        
        elif x > 0:
            return computeReverse(x)
        
        x = x * -1
        return -1 * computeReverse(x)