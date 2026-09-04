class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # for i in range(len(nums)):
        #     m=max(nums[:i+1])
        #     n=min(nums[i:])
        #     score=m-n
        #     if score<=k:
        #         return i
        # return -1
        n=len(nums)
        pre_max=[0]*n
        pre_max[0]=nums[0]
        for i in range(1, n):
            pre_max[i]=max(pre_max[i-1], nums[i])
        suf_min=[0]*n
        suf_min[-1]=nums[-1]
        for i in range(n-2, -1, -1):
            suf_min[i]=min(suf_min[i+1], nums[i])
        for i in range(n):
            score= pre_max[i]-suf_min[i]
            if score<=k:
                return i
        return -1