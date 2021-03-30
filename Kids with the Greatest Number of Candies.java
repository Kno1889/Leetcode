class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int highest = 0;
        
        for(int i = 0; i < candies.length; i++){
            if(candies[i] >= highest)
                highest = candies[i];
            
        }
        
        List<Boolean> boolList = new ArrayList<Boolean>();
        
        for(int i = 0; i < candies.length; i++){
            if(candies[i] + extraCandies >= highest)
                boolList.add(true);
            else
                boolList.add(false);
        }
        
        return boolList;
    }
}
