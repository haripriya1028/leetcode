class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s==goal){
            return true;
        }
        int k=0;
        int i=1;
        while(k<s.size()){
            s= s.substr(1) + s.substr(0, 1);
            k++;
            if(s==goal){
                return true;
            }
        }
        return false;
    }
};