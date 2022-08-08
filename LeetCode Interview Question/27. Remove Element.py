from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #match the number in the list
        #if it's match just shift left the number, it should be less space complexity
        #take a for loop ,
        #WE JUST use l variable, and other numbers wont store
        l=0


        for r in range(0,len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l = l+1

        return  l


a1= Solution()
a1.removeElement([0,1,2,2,3,0,4,2], 2)