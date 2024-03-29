class Solution {
    public boolean isPalindrome(int x) {
        //int[] str = new str[];
        //int[] rev = new str[];
        
        int rev = 0;
        int val = x;
        
        if(x < 0 || (x % 10 == 0 && x != 0))
            return false;
        
        while(x != 0){
            int dig = x % 10;
            rev = rev * 10 + dig;
            x = x / 10;
        }
        
        return val == rev;
               
    }
}
