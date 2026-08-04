class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        res=[]
        for i in range(min(nums), max(nums)):
            if i not in seen:
                res.append(i)
        return res