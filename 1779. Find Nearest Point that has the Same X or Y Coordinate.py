class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        def get_dist(point: List[int]) -> int:
            return abs(point[0] - x) + abs(point[1] - y)
        
        def is_valid(point: List[int]) -> bool:
            return point[0] == x or point[1] == y

        min_dist = float("inf")

        for i in range(len(points) - 1, -1, -1):
            if is_valid(points[i]) and get_dist(points[i]) <= min_dist:
                min_dist = get_dist(points[i])
                min_ind = i
        
        if min_dist == float("inf"):
            return -1
        return min_ind
       