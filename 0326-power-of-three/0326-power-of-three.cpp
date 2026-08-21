class Solution {
public:
    bool isPowerOfThree(int n) {
        return findAns(n);
    }
    bool findAns(int n){
        if(n==1){
            return true;
        }else if(n<1 || n%3!=0 ){
            return false;
        }
        
        return findAns(n/3);
    }
};