class Solution {
    public int[] decompressRLElist(int[] nums) {
        int origLen = nums.length;
        int newLen = 0; 
        
        for(int i = 0;i < origLen;i += 2)
            newLen += nums[i];
            
        int[] newArr = new int[newLen]; 
        int Ind = 0; 
        
        for(int i = 0 ; i < origLen; i += 2){
            for(int j = 0 ; j < nums[i] ; j++)
                newArr[Ind++] = nums[i + 1];
        }
        return newArr;
    }
}
