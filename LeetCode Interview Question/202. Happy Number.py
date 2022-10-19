class Solution:
    def isHappy(self, n: int) -> bool:
        var = set()
        while n not in var:
            var.add(n)
            n = self.sumOfSquare(n)
            print(n)
            if n == 1:
                return True
        return False
    def sumOfSquare(self,num) -> int:
        output = 0
        while num:
            digit = num % 10
            digit = digit ** 2
            output = output + digit
            num = num // 10
        return output


a1 = Solution()
print(a1.isHappy(19))
