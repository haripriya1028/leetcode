class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        for n in seen:
            if n-1 not in seen:
                curr=n
                length=1
                while curr+1 in seen:
                    curr+=1
                    length+=1
                longest=max(length, longest)
        return longest