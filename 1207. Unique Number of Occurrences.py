class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for i in arr:
            count[i] = count.get(i, 0) + 1
        
        return sorted(list(set(count.values()))) == sorted(count.values())
        