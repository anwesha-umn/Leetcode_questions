class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // sorted array duplicates - means they should be adjacent to each other 

        // create a new start index k - for non-repeating elememts
        int k = 0;
        for (int i=0; i < nums.size()-1; i++){
            if (nums[i] != nums[i+1]){
                nums[k] = nums[i];
                k+=1;
            }
        nums[k] = nums[i+1];
        }
        return k+1;
    }
};