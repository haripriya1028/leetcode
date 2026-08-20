class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        l=0
        count=0
        maxLen=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            
            while freq[s[r]]>2:
                #while a letter is repeated more than twice
                freq[s[l]]-=1
                l+=1
                
            count=r-l+1
            maxLen=max(count,maxLen)
        return maxLen
