class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        k=0
        i=1
        while k<len(s):
            s=s[i:]+s[:i]
            k+=1
            if s==goal:
                return True
        return False