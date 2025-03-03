class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
            if area > max_area:
                max_area = area
        
        return max_area
