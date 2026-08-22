class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dsum=0
        dprod=1
        num=n
        while num!=0:
            dsum+=num%10
            dprod*=num%10
            num//=10
        totalSum=dsum+dprod
        if n%totalSum==0:
            return True
        else:
            return False

