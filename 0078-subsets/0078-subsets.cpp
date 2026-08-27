class Solution {
public:
    void createSubset(int i, vector<int> &nums, vector<vector<int>> &result, vector<int> &subset){
        if(i==nums.size()){
            result.push_back(subset);
            return;
        }
        subset.push_back(nums[i]);
        createSubset(i+1, nums, result, subset);
        subset.pop_back();
        createSubset(i+1, nums, result, subset);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;
        createSubset(0, nums, result, subset);
        return result;
    }
    
};
// result=[]
//         subset=[]
//         def createSubset(i):
//             if i==len(nums):
//                 result.append(subset[:])
//                 return
//             subset.append(nums[i])
//             createSubset(i+1)
//             subset.pop()
//             createSubset(i+1)
//         createSubset(0)
//         return result