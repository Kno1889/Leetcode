class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # simpler that it seems: just find the max diff in x coords
        # b/w 2 adjacent points
        # => sort O(nlogn) and then iterate O(n)

        points.sort()
        max_width = 0
        for i in range(len(points) - 1): # comparing i to i + 1
            width = points[i + 1][0] - points[i][0]
            if width > max_width:
                max_width = width
        
        return max_width
        