class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-num for num in nums]
        heapq.heapify(nums)
        l=(len(nums)-k)+1
        while len(nums)>l:
            heapq.heappop(nums)
        return -heapq.heappop(nums)