class Solution:
    def trap(self, height: List[int]) -> int:
        # limiting factor: min of left and right height
        # at each index i, trap min(L, R) - h[i]
        # relevant L, R is max L and max R
        # O(n) time, O(1) mem sol: use pointers to keep track of max

        max_L = height[0]
        max_R = height[-1]
        l, r = 0, len(height) - 1
        water = 0
        # shift smaller one

        while l < r:
            if max_L < max_R:
                l += 1
                max_L = max(max_L, height[l]) # auto handle non-negative
                water += max_L - height[l]
            else:
                r -= 1
                max_R = max(max_R, height[r])
                water += max_R - height[r]
        
        return water
