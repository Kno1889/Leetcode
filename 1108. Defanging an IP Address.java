class Solution {
    public String defangIPaddr(String address) {
        String newAddress = "";
        
        for(int i = 0; i < address.length(); i++){
            if(address.charAt(i) != '.')
                newAddress += address.charAt(i);
            
            if(address.charAt(i) == '.')
                newAddress += "[.]";
        }
        
        return newAddress;
    }
}
