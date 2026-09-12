class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        res = [0]*(len(num1)+len(num2))
        for p1 in range(len(num1)):
            for p2 in range(len(num2)):
                digit = int(num1[p1]) * int(num2[p2])
                res[p1+p2] += digit
                res[p1+p2+1] += (res[p1+p2]//10)
                res[p1+p2] = res[p1+p2]%10
        res, st = res[::-1], 0
        while st < len(res) and res[st]==0:
            st+=1
        
        res = map(str, res[st:])
        return "".join(res)

