class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        
        # easiest solution is using dictionaries
        indices = {"type": 0, "color": 1, "name": 2}
        count = 0
        
        for i in range(len(items)): 
            if(items[i][indices[ruleKey]] == ruleValue):
                count+=1
        return count
