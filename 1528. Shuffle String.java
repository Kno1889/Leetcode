class Solution {
    public String restoreString(String s, int[] indices) {
        int sLen = s.length();
        String shuffled = "";
        char[] shuff = new char[sLen];
        
        for(int i = 0; i < sLen; i++)
            shuff[indices[i]] = s.charAt(i);
        
        for(int i = 0; i < sLen; i++)
            shuffled += shuff[i];
        
        return shuffled;
        
    }
}
