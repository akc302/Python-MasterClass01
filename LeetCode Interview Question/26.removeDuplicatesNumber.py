from typing import List


class Solution:
    def removeDuplicates(self,nums: List[int]) -> int:
        ###delete duplicate value
        ###compute the lenth
        #place '_" in the postn where the value is deleted

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l = l + 1

        print(l)
        print(nums)
        return l

a1 = Solution()

a1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])





