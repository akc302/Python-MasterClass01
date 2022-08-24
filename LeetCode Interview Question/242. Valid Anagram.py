class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for i in range(len(s)):
            if countS[s[i]] != countT.get(s[i],0):
                return False
        return True


a1 = Solution()
print(a1.isAnagram("rat", "car"))


