from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff], i]
            if diff not in hashmap:
                hashmap[n] = i
        return

a1 = Solution()
print(a1.twoSum([-1,-2,-3,-4,-5],
-8))

