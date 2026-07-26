class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        count=0
        while left<=right:
            diff=limit-people[right]
            right-=1
            count+=1
            if left<=right and diff>=people[left]:
                left+=1
        return count