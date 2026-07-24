class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix=0
        freq={0:1}
        for n in nums:
            prefix+=n
            if prefix-k in freq:
                count+=freq[prefix-k]
            freq[prefix]=freq.get(prefix,0)+1
        return count