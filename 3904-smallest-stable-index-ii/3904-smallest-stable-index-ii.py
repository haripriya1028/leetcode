class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        premax=[0]*n
        premax[0]=nums[0]
        for i in range(1, n):
            premax[i]=max(premax[i-1], nums[i])
        sufmin=[0]*n
        sufmin[-1]=nums[-1]
        for i in range(n-2, -1, -1):
            sufmin[i]=min(sufmin[i+1], nums[i])
        for i in range(n):
            score=premax[i]-sufmin[i]
            if score<=k:
                return i
        return -1