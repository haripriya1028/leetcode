class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int i=1;
        while(nums_set.count(i*k)){
            i++;
        }
        return i*k;
    }
};