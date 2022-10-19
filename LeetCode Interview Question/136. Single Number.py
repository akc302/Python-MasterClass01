
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0

        for i in range(0,len(nums),1):
            res = nums[i] ^ res  #xor operations
            #print(bin(res))
        return res

a1 =Solution()
print(a1.singleNumber([4,1,2,1,2]))



