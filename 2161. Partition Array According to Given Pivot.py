class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        greater_than = []
        pivots = []

        for n in nums:
            if n < pivot:
                less_than.append(n)
            elif n == pivot:
                pivots.append(n)
            else:
                greater_than.append(n)
        
        return less_than + pivots + greater_than
        