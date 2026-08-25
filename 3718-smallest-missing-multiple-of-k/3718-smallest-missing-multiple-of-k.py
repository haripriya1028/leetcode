class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # i=1
        # while i*k in nums:
        #     i+=1
        # return i*k
        nums_set=set(nums)
        i=1
        while i*k in nums_set:
            i+=1
        return i*k