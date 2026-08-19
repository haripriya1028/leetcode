class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved={}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row]=set()
            reserved[row].add(seat)
        count=total = 2 * (n - len(reserved))
        for seats in reserved.values():

            left=all(s not in seats for s in [2,3,4,5])
            mid=all(s not in seats for s in [4,5,6,7])
            right=all(s not in seats for s in [6,7,8,9])

            if left and right:
                count+=2
            elif left or right or mid:
                count+=1
        return count