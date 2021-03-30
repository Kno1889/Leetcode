class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] outArr = new int[2 * n];
        
        int j = n; 
        int Ind = 0;
        
        for(int i = 0; i < n; i++){
            outArr[Ind++] = nums[i];
            outArr[Ind++] = nums[j++];
        }
        
        return outArr;
    }  
}
