from itertools import permutations
from itertools import combinations
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        perm = combinations([1,2,3], n)
        print(perm)

        stack = []
        res = []
        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            if open <n :
                stack.append("(")
                backtrack(open+1,close)
                stack.pop()

            if close < open :
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return res


a1 =Solution()
l1 = a1.generateParenthesis(4)
print(l1)