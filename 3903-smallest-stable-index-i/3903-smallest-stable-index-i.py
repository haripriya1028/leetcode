class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            m=max(nums[:i+1])
            n=min(nums[i:])
            score=m-n
            if score<=k:
                return i
        return -1