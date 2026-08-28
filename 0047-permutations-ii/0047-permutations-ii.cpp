class Solution {
public:
    void perms(int i, vector<int>& nums, vector<vector<int>>& result){
        unordered_set<int> seen;
        if(i==nums.size()){
            result.push_back(nums);
            return;
        }
        for(int j=i; j<nums.size(); j++){
            if(seen.find(nums[j]) != seen.end()){
                continue;
            }
            seen.insert(nums[j]);
            swap(nums[i], nums[j]);
            perms(i+1, nums, result);
            swap(nums[i], nums[j]);
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        perms(0, nums, result);
        return result;
    }
};