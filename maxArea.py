class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            h = min(height[l], height[r])
            best = max(best, h * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best


height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height1))

height2 = [1, 1]
print(Solution().maxArea(height2))
