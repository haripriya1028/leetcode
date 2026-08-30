class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int i;
        int indexmax=0; 
        int indexmin=0;
        int n=nums.size();
        for(i=0; i<nums.size(); i++){
            if(nums[i]>nums[indexmax]){
                indexmax=i;
            }
            if(nums[i]<nums[indexmin]){
                indexmin=i;
            }
        }
        int j=min(indexmax, indexmin);
        int k=max(indexmax, indexmin);
        int res=min({n-j, k+1, j+1+n-k});
        return res;


    }
};