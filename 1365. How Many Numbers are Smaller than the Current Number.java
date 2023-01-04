class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int lenArr = nums.length;
        int[] smallerThan = new int[lenArr];
        int numSmaller = 0;
        
        for(int i = 0; i < lenArr; i++){
            for(int j = 0; j < lenArr; j++){
                if(nums[j] < nums[i] && i != j)
                    numSmaller++;
            }
            smallerThan[i] = numSmaller;
            numSmaller = 0;
        }
        return smallerThan;
    }
}
