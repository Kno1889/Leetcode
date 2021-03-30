class Solution {
    public int[] runningSum(int[] nums) {
        int arrLen = nums.length;
        int[] runningSumArr = new int[arrLen];
        
        runningSumArr[0] = nums[0];
        
        for(int i = 1; i < arrLen; i++){
            runningSumArr[i] = nums[i];
        }
        
        for(int i = 1; i < arrLen; i++){
            runningSumArr[i] += runningSumArr[i - 1];
        }
        return runningSumArr;
    }
}
