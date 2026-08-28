class Solution {
public:
    void solve(int i, vector<int>& candidates, int target, vector<int>& combination, vector<vector<int>>& result){
        if(target==0){
            result.push_back(combination);
            return;
        }
        if(i==candidates.size()){
            return;
        }
        if(candidates[i]<=target){
            combination.push_back(candidates[i]);
            solve(i, candidates, target-candidates[i], combination, result);
            combination.pop_back();
        }
        solve(i + 1, candidates, target, combination, result);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> combination;
        vector<vector<int>> result;
        solve(0, candidates, target, combination, result);
        return result;
    }
};