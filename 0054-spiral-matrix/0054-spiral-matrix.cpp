class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rows=matrix.size();
        int cols=(matrix[0]).size();
        int top=0;
        int bottom=rows-1;
        int left=0;
        int right=cols-1;
        vector<int> res;
        while(top<=bottom && left<=right){
            for(int j=left; j<=right; j++){
                res.push_back(matrix[top][j]);
                
            }
            top++;
            for(int i=top; i<=bottom; i++){
                res.push_back(matrix[i][right]);
                
            }
            right--;
            if(top<=bottom){
                for(int i=right; i>=left; i--){
                    res.push_back(matrix[bottom][i]);
                }
                bottom--;
            }
            if(left<=right){
                for(int j=bottom; j>=top; j--){
                    res.push_back(matrix[j][left]);
                }
                left++;
            }
        }
        
        return res;

    }
};