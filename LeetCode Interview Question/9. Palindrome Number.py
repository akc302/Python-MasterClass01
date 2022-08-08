class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(str(x)[::-1])
        if str(x) == str(x)[::-1]:
            return True
        return False

a1 =Solution()
a1.isPalindrome(122)